# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(658, 662)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        form.setFont(font)
        self.centralwidget = QtWidgets.QWidget(form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 631, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.db_text = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.db_text.setMaximumSize(QtCore.QSize(16777215, 49))
        self.db_text.setFrameShape(QtWidgets.QFrame.Panel)
        self.db_text.setObjectName("db_text")
        self.gridLayout.addWidget(self.db_text, 0, 1, 1, 1)
        self.opendb_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.opendb_btn.setMinimumSize(QtCore.QSize(99, 0))
        self.opendb_btn.setMaximumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.opendb_btn.setFont(font)
        self.opendb_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.opendb_btn.setObjectName("opendb_btn")
        self.gridLayout.addWidget(self.opendb_btn, 0, 0, 1, 1)
        self.openfile_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openfile_btn.setMaximumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openfile_btn.setFont(font)
        self.openfile_btn.setObjectName("openfile_btn")
        self.gridLayout.addWidget(self.openfile_btn, 1, 0, 1, 1)
        self.file_text = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.file_text.setMaximumSize(QtCore.QSize(16777215, 49))
        self.file_text.setFrameShape(QtWidgets.QFrame.Panel)
        self.file_text.setObjectName("file_text")
        self.gridLayout.addWidget(self.file_text, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 160, 631, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dbupdate_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dbupdate_btn.setMinimumSize(QtCore.QSize(99, 49))
        self.dbupdate_btn.setMaximumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dbupdate_btn.setFont(font)
        self.dbupdate_btn.setAutoRepeat(False)
        self.dbupdate_btn.setObjectName("dbupdate_btn")
        self.gridLayout_2.addWidget(self.dbupdate_btn, 0, 1, 1, 1)
        self.dataselect_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.dataselect_btn.setMinimumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dataselect_btn.setFont(font)
        self.dataselect_btn.setObjectName("dataselect_btn")
        self.gridLayout_2.addWidget(self.dataselect_btn, 0, 3, 1, 1)
        self.quit_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.quit_btn.setMinimumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quit_btn.setFont(font)
        self.quit_btn.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.quit_btn.setObjectName("quit_btn")
        self.gridLayout_2.addWidget(self.quit_btn, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 6, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 590, 631, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 631, 91))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableclear_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.tableclear_btn.setMinimumSize(QtCore.QSize(99, 49))
        self.tableclear_btn.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableclear_btn.setFont(font)
        self.tableclear_btn.setObjectName("tableclear_btn")
        self.gridLayout_3.addWidget(self.tableclear_btn, 1, 9, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setMinimumSize(QtCore.QSize(99, 49))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.point_text = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.point_text.setMinimumSize(QtCore.QSize(99, 49))
        self.point_text.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.point_text.setFont(font)
        self.point_text.setAlignment(QtCore.Qt.AlignCenter)
        self.point_text.setObjectName("point_text")
        self.gridLayout_3.addWidget(self.point_text, 1, 4, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.search_btn.setMinimumSize(QtCore.QSize(99, 49))
        self.search_btn.setMaximumSize(QtCore.QSize(99, 49))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_3.addWidget(self.search_btn, 1, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 8, 1, 1)
        self.line_text = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.line_text.setMinimumSize(QtCore.QSize(99, 49))
        self.line_text.setMaximumSize(QtCore.QSize(99, 16777215))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line_text.setFont(font)
        self.line_text.setAlignment(QtCore.Qt.AlignCenter)
        self.line_text.setObjectName("line_text")
        self.gridLayout_3.addWidget(self.line_text, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 4, 1, 1)
        self.output_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(10, 370, 631, 192))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        self.output_text.setFont(font)
        self.output_text.setObjectName("output_text")
        form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 23))
        self.menubar.setObjectName("menubar")
        self.menuProject = QtWidgets.QMenu(self.menubar)
        self.menuProject.setObjectName("menuProject")
        form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        form.setStatusBar(self.statusbar)
        self.actionDatabase = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        self.actionDatabase.setFont(font)
        self.actionDatabase.setObjectName("actionDatabase")
        self.actionQuit = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(10)
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.menuProject.addAction(self.actionDatabase)
        self.menuProject.addSeparator()
        self.menuProject.addAction(self.actionQuit)
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "DataBase"))
        self.opendb_btn.setText(_translate("form", "Database"))
        self.openfile_btn.setText(_translate("form", "File"))
        self.dbupdate_btn.setText(_translate("form", "Update DB"))
        self.dataselect_btn.setText(_translate("form", "Data Select"))
        self.quit_btn.setText(_translate("form", "Quit"))
        self.tableclear_btn.setText(_translate("form", "Clear TB"))
        self.point_text.setText(_translate("form", "0"))
        self.search_btn.setText(_translate("form", "Search"))
        self.line_text.setText(_translate("form", "0"))
        self.label.setText(_translate("form", "Line"))
        self.label_2.setText(_translate("form", "Point"))
        self.menuProject.setTitle(_translate("form", "Database"))
        self.actionDatabase.setText(_translate("form", "Create_Database"))
        self.actionQuit.setText(_translate("form", "Quit"))

