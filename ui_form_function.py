from mainwindowform import Ui_form
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import config
import filefunction
from dbfunction import Table
from SpsParser import Sps21Parser
from dbprocess import DbUpdate, DbSelect, DbXUpdate
from PyQt5.QtCore import QThreadPool
import logging
from importlib import reload


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_form()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

        self.ui.actionDatabase.triggered.connect(self.create_db)
        self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.ui.opendb_btn.clicked.connect(self.open_db)
        self.ui.openfile_btn.clicked.connect(self.open_sps)

        self.ui.dbupdate_btn.clicked.connect(self.__update_db)
        self.ui.dataselect_btn.clicked.connect(self.__select_from_db)
        self.ui.quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.ui.search_btn.clicked.connect(self.__search)
        self.ui.tableclear_btn.clicked.connect(self.clear_tab)

        self.db_file = None
        self.sps_file = None
        self.ui.progressBar.setValue(0)
        self.ui.comboBox.addItems(config.table_dict.keys())

    def create_db(self):
        previous_db_file = self.db_file
        self.db_file = filefunction.file_save(self, previous_db_file, config.db_file_pattern)
        if not self.db_file:
            return

        if not self.db_file.endswith('.sqlite'):
            self.db_file += '.sqlite'
        db = Table(self.db_file)
        print(db)
        db.table_crate()

    def open_db(self):
        """
            Opens DB file
        """
        previous_db_file = self.db_file
        self.db_file = filefunction.file_open(self, previous_db_file, config.db_file_pattern)
        self.ui.db_text.setText(self.db_file)

    def open_sps(self):
        """
            Opens SPS file
        """
        previous_sps_file = self.ui.file_text.setText(self.sps_file)
        self.sps_file = filefunction.file_open(self, previous_sps_file, config.sps_file_pattern)
        self.ui.file_text.setText(self.sps_file)
        self.__prepare_logging()
        self.to_file = self.sps_file + '.output'

    def runner(self):
        db = Table(self.db_file)
        conn = db.create_connection()
        current_table = db.choose_table(self.sps_file)
        parser = Sps21Parser()

        with open(self.sps_file) as f:
            for line in f:
                parsed = parser.parse_point(line)
                if parsed is not None:
                    key_list = [parsed[1], parsed[2], parsed[3]]
                    get_record = db.get_record_for_point(conn, current_table, key_list)
                    print(get_record)

    def __update_db(self):
        try:
            db = Table(self.db_file)
            conn = db.create_connection()
            #            worker = DbUpdate(self.db_file, conn, self.sps_file)
            worker = DbXUpdate(self.db_file, conn, self.sps_file)
            self.threadpool.start(worker)
            worker.signals.start.connect(self.__process_start)
            worker.signals.process_max.connect(self.__progress_max)
            worker.signals.process.connect(self.__processing)
            worker.signals.finished.connect(self.__processed)
        except Exception as e:
            print(str(e))
            self.__log('update_db :' + str(e))

    def __select_from_db(self):
        try:
            db = Table(self.db_file)
            conn = db.create_connection()
            current_table = self.ui.comboBox.currentText()
            worker = DbSelect(self.db_file, conn, current_table, self.sps_file, self.to_file)
            self.threadpool.start(worker)
            worker.signals.start.connect(self.__process_start)
            worker.signals.process_max.connect(self.__progress_max)
            worker.signals.process.connect(self.__processing)
            worker.signals.finished.connect(self.__processed)
        except Exception as e:
            print(str(e))
            self.__log('update_db :' + str(e))

    def __search(self):
        line = float(self.ui.line_text.text())
        point = float(self.ui.point_text.text())
        try:
            db = Table(self.db_file)
            conn = db.create_connection()
            with conn:
                c = conn.cursor()
                current_table = self.ui.comboBox.currentText()
                if line > 0 and point > 0:
                    c.execute("SELECT * FROM " + current_table + " WHERE line =? and point = ? and idx = ?",
                              (line, point, 1))
                else:
                    c.execute("SELECT * FROM " + current_table)
                rows = c.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        self.ui.output_text.append(str(row))
                else:
                    self.ui.output_text.setText('Not exist')
        except Exception as e:
            print(str(e))
            self.__log('update_db :' + str(e))

    def clear_tab(self):
        db = Table(self.db_file)
        conn = db.create_connection()
        current_table = self.ui.comboBox.currentText()
        QMessageBox.question(self, 'Question', 'Do you really want to clear whole table ?',
                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if QMessageBox.Yes:
            db.clear(conn, current_table)
            self.__log('table %s is cleared' % current_table)

    def __process_start(self, stat: bool):
        self.__btn_enable(stat)
        self.ui.progressBar.setValue(0)

    def __progress_max(self, line_counter):
        self.ui.progressBar.setMaximum(line_counter)
        self.__log('maxline%d' % line_counter)

    def __processing(self, counter):
        self.ui.progressBar.setValue(counter)
        #        self.ui.output_text.append('progress%d' % counter)
        self.__log('progress%d' % counter)

    def __processed(self, stat: bool):
        self.__btn_enable(stat)

    def __prepare_logging(self):
        logging.shutdown()
        reload(logging)
        log_filename = self.sps_file + '.log'
        log_format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename=log_filename, filemode='a', format=log_format, level=logging.NOTSET)
        logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

    def __log(self, msg: str):
        logging.info(msg)

    def __btn_enable(self, stat: bool):
        self.ui.opendb_btn.setEnabled(stat)
        self.ui.openfile_btn.setEnabled(stat)
        self.ui.dbupdate_btn.setEnabled(stat)
        self.ui.dataselect_btn.setEnabled(stat)
        self.ui.quit_btn.setEnabled(stat)
        self.ui.search_btn.setEnabled(stat)
        self.ui.tableclear_btn.setEnabled(stat)

    # def comm(self, conn):
    #     conn.commit

    # db = Table(self.db_file)
    # conn = db.create_connection()
    # current_table = db.choose_table(self.sps_file)
    # parser = Sps21Parser()
    # conn.execute("PRAGMA synchronous=OFF")  # 关闭同步
    # conn.execute("BEGIN TRANSACTION")  # 显式开启事务
    #
    # counter = 1
    # with open(self.sps_file) as f:
    #     for line in f:
    #         parsed = parser.parse_point(line)
    #         if parsed is not None:
    #             db.db_point_update(conn, current_table, parsed)
    #             if counter % self.commit_every == 0:
    #                 conn.commit()
    #             counter += 1
    # conn.commit()
    # conn.close()

    # # self.DB_TABLE = db.choose_table(self.sps_file)
    # paser = Sps21Parser()
    # if self.db_file and self.sps_file:
    #     self.DB_TABLE = str.upper(self.db.choose_table(self.sps_file))
    #     with open(self.sps_file) as sps:
    #         for line in sps:
    #             pasered = paser.parse_point(line)
    #             if pasered:
    #                 Table.insert_record_from_parsed_sps(conn, self.DB_TABLE, pasered)
    #
    #     dbprocess.process(self.db_file, self.DB_TABLE, self.sps_file)
    #
    # # print(dbupdate1.process( self.db_file, self.DB_TABLE, self.sps_file))
    #
    # else:
    #     print('error process')
    # QMessageBox.information(self,
    #                         "updated number",
    #                         str(dbprocess.process(self.db_file, self.DB_TABLE, self.sps_file)),
    #                         QMessageBox.Yes | QMessageBox.No)
