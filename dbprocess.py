import dbfunction
from SpsParser import Sps21Parser
import os
import check
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
from dbfunction import Table
import time


class DbUpdate(QRunnable):
    def __init__(self, db_file, conn, file_name):
        super().__init__()
        self.conn = conn
        self.file_name = file_name
        self.db_file = db_file

        self.signals = WorkerSignal()
        self.db = Table(self.db_file)
        self.parser = Sps21Parser()

    @pyqtSlot()
    def run(self):

        self.signals.start.emit(False)
        line_numbers = check.iter_count(self.file_name)
        # print(line_numbers)
        self.signals.process_max.emit(line_numbers)
        table_name = self.db.choose_table(self.file_name)
        self.conn.execute("PRAGMA synchronous=OFF")  # 关闭同步
        self.conn.execute("BEGIN TRANSACTION")  # 显式开启事务
        counter = 0
        try:
            c = self.conn.cursor()
            with open(self.file_name) as fr:
                for line in fr:
                    parsed = self.parser.parse_point(line)
                    if parsed:
                        sql_insert = "INSERT OR REPLACE INTO " + table_name + " (line, point, idx, easting, northing, elevation) VALUES (?, ?, ?, ?, ?, ?);"
                        data = covert_parsed_to_point(parsed)
                        c.execute(sql_insert, data)
                    counter += 1
                    if counter % 100000 == 0:
                        self.signals.process.emit(counter)
                        self.conn.commit()
        except Exception as e:
            print(str(e))
        self.signals.process.emit(counter)
        self.signals.finished.emit(True)
        self.conn.commit()
        c.close()


class DbXUpdate(QRunnable):
    def __init__(self, db_file, conn, file_name):
        super().__init__()
        self.conn = conn
        self.file_name = file_name
        self.db_file = db_file

        self.signals = WorkerSignal()
        self.db = Table(self.db_file)
        self.parser = Sps21Parser()

    @pyqtSlot()
    def run(self):

        self.signals.start.emit(False)
        line_numbers = check.iter_count(self.file_name)
        self.signals.process_max.emit(line_numbers)
        table_name = self.db.choose_table(self.file_name)
        self.conn.execute("PRAGMA synchronous=OFF")  # 关闭同步
        self.conn.execute("BEGIN TRANSACTION")  # 显式开启事务
        counter = 0
        tcounter = 0
        try:
            c = self.conn.cursor()
            osln = 0
            ospn = 0
            osidx = 0
            with open(self.file_name) as fr:
                for line in fr:
                    counter += 1
                    parsed = self.parser.parse_relation(line)
                    if parsed:
                        xps = convert_parsed_to_xps(parsed)
                        sln = parsed[5]
                        spn = parsed[6]
                        spidx = parsed[7]
                        if sln == osln and spn == ospn and spidx == osidx:
                            relation.append(xps)
                        else:
                            if osln != 0:
                                sql_insert = "INSERT OR REPLACE INTO " + table_name + " (line, point, idx, relation) VALUES (?, ?, ?, ?);"
                                data = (osln, ospn, osidx, str(relation))
                                c.execute(sql_insert, data)
                                tcounter += 1
                            relation = []
                            relation.append(xps)
                            osln = sln
                            ospn = spn
                            osidx = spidx

                        if tcounter % 10000 == 0:
                            self.signals.process.emit(counter)
                            self.conn.commit()

                if osln != 0:
                    sql_insert = "INSERT OR REPLACE INTO " + table_name + " (line, point, idx, relation) VALUES (?, ?, ?, ?);"
                    data = (osln, ospn, osidx, str(relation))
                    c.execute(sql_insert, data)

        except Exception as e:
            print(str(e))
        self.signals.process.emit(counter)
        self.signals.finished.emit(True)
        self.conn.commit()
        c.close()


class DbSelect(QRunnable):
    def __init__(self, db_file, conn, table_name, from_file_name, to_file_name):
        super().__init__()
        self.db_file = db_file
        self.conn = conn
        self.table_name = table_name
        self.from_file_name = from_file_name
        self.to_file_name = to_file_name

        self.signals = WorkerSignal()
        self.db = Table(self.db_file)
        self.parser = Sps21Parser()

    @pyqtSlot()
    def run(self):
        self.signals.start.emit(False)
        line_numbers = check.iter_count(self.from_file_name)
        self.signals.process_max.emit(line_numbers)
        db = Table(self.db_file)
        counter = 0
        try:
            with open(self.from_file_name) as fr:
                with open(self.to_file_name, 'w') as tf:
                    for line in fr:
                        parsed = self.parser.parse_point(line)
                        if parsed:
                            list = [parsed[1], parsed[2], parsed[3]]
                            data = db.get_record_for_point(self.conn, self.table_name, list)
                            tf.write(str(data) + '\n')
                        counter += 1
                        if counter % 10000 == 0:
                            self.signals.process.emit(counter)

        except Exception as e:
            print(str(e))
        self.signals.process.emit(counter)
        self.signals.finished.emit(True)


class WorkerSignal(QObject):
    start = pyqtSignal(bool)
    process = pyqtSignal(int)
    process_max = pyqtSignal(int)
    finished = pyqtSignal(bool)


class Template:
    def __init__(self):
        self.sline = 0.0
        self.spoint = 0.0
        self.sidx = 0
        self.relations = []


class Xps:
    def __init__(self):  # sline, spoint, sidx, from_ch, to_ch, rline, from_rp, to_rp, ridx
        self.sline = 0.0
        self.spoint = 0.0
        self.sidx = 0
        self.from_ch = 0
        self.to_ch = 0
        self.rline = 0.0
        self.from_rp = 0.0
        self.to_rp = 0.0
        self.ridx = 0


def covert_parsed_to_point(parsed: list):
    line = parsed[1]
    point = parsed[2]
    idx = parsed[3]
    easting = parsed[10]
    northing = parsed[11]
    elevation = parsed[12]
    if elevation == None:
        elevation = 0
    data = (line, point, idx, easting, northing, elevation)
    return data


def convert_parsed_to_xps(parsed: list):
    sline = parsed[5]
    spoint = parsed[6]
    sidx = parsed[7]
    from_ch = parsed[8]
    to_ch = parsed[9]
    rline = parsed[11]
    from_rp = parsed[12]
    to_rp = parsed[13]
    ridx = parsed[14]
    xps = [sline, spoint, sidx, from_ch, to_ch, rline, from_rp, to_rp, ridx]
    return xps
