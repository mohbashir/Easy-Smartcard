# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 411)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnConnect = QtWidgets.QPushButton(self.centralWidget)
        self.btnConnect.setGeometry(QtCore.QRect(430, 60, 91, 21))
        self.btnConnect.setObjectName("btnConnect")
        self.comboReaders = QtWidgets.QComboBox(self.centralWidget)
        self.comboReaders.setGeometry(QtCore.QRect(80, 60, 341, 21))
        self.comboReaders.setObjectName("comboReaders")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(140, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtCAPDU = QtWidgets.QLineEdit(self.centralWidget)
        self.txtCAPDU.setGeometry(QtCore.QRect(80, 130, 371, 22))
        self.txtCAPDU.setObjectName("txtCAPDU")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 41, 20))
        self.label_3.setObjectName("label_3")
        self.lblATR = QtWidgets.QLabel(self.centralWidget)
        self.lblATR.setGeometry(QtCore.QRect(80, 90, 421, 16))
        self.lblATR.setText("")
        self.lblATR.setObjectName("lblATR")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 41, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 41, 20))
        self.label_5.setObjectName("label_5")
        self.btnSend = QtWidgets.QPushButton(self.centralWidget)
        self.btnSend.setGeometry(QtCore.QRect(460, 130, 61, 21))
        self.btnSend.setObjectName("btnSend")
        self.listRAPDU = QtWidgets.QListWidget(self.centralWidget)
        self.listRAPDU.setGeometry(QtCore.QRect(80, 160, 441, 201))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.listRAPDU.setFont(font)
        self.listRAPDU.setObjectName("listRAPDU")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 542, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Smartcard"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Readers"))
        self.label_2.setText(_translate("MainWindow", "Easy Smartcard "))
        self.label_3.setText(_translate("MainWindow", "CAPDU"))
        self.label_4.setText(_translate("MainWindow", "RAPDU"))
        self.label_5.setText(_translate("MainWindow", "ATR"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
