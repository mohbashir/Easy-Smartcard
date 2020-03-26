import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
import threading
from smartcard.System import readers
from smartcard.util import HexListToBinString, toHexString, toBytes

class MainWindow(QMainWindow):

    global connection

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('mainwindow.ui', self)
        self.readerList = readers()
        self.fillComboBox()

        self.actionAbout.triggered.connect(self.showAbout)
        self.actionExit.triggered.connect(lambda:QApplication.quit())

        self.btnConnect.clicked.connect(self.connectToCard)
        self.btnSend.clicked.connect(self.sendAPDU)

    def showAbout(self):
        QMessageBox.question(self, 'About', "Easy Smartcard v0.1\n\nConnect to smartcard get atr\n"
                                            "send APDU command and return RAPDU response\n\n"
                                            "Developed by : Mohammed Bashir\n"
                                            "Phone : +966 55 0918 242", QMessageBox.Ok)

    def fillComboBox(self):
        for readerIndex, readerItem in enumerate(self.readerList):
            print(readerIndex, readerItem)
            self.comboReaders.addItem(str(readerItem))

    def connectToCard(self):
        try:
            reader = self.readerList[self.comboReaders.currentIndex()]
            self.connection = reader.createConnection()
            self.connection.connect()
            atr = self.connection.getATR()
            self.lblATR.setText(toHexString(atr))
        except:
            print("error")

    def sendAPDU(self):
        strAPDU = self.txtCAPDU.text()

        bytesAPDU = toBytes(strAPDU)
        data, sw1, sw2 = self.connection.transmit(bytesAPDU)

        self.listRAPDU.addItem("<< " + strAPDU)
        self.listRAPDU.addItem(">> " + toHexString(data) + " (%02X %02X)" % (sw1, sw2))
        self.listRAPDU.addItem("")
        # self.txtCAPDU.clear()

app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())