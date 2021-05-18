# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import telnetlib
from time import sleep
colors = {
	"green" : "",
	"blue" : "",
	"darkblue" : "",
	"darkred" : "",
	"gold" : "",
	"lightgreen" : "",
	"lightred" : "",
	"lime" : "",
	"orchid" : "",
}
tn2 = telnetlib.Telnet("127.0.0.1", 2121)

def run(command):
	cmd_s = command + "\n"
	tn2.write(cmd_s.encode('utf-8'))
	sleep(0.005)


class Ui_coloredtxt(object):
    def setupUi(self, coloredtxt):
        if not coloredtxt.objectName():
            coloredtxt.setObjectName(u"coloredtxt")
        coloredtxt.resize(431, 120)
        coloredtxt.setMinimumSize(QSize(401, 120))
        coloredtxt.setMaximumSize(QSize(431, 120))
        self.plainTextEdit = QPlainTextEdit(coloredtxt)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 411, 71))
        self.Green = QPushButton(coloredtxt)
        self.Green.setObjectName(u"Green")
        self.Green.setGeometry(QRect(10, 90, 21, 23))
        self.Green.setStyleSheet(u"background: rgb(64, 255, 64)")
        self.lightblue = QPushButton(coloredtxt)
        self.lightblue.setObjectName(u"lightblue")
        self.lightblue.setGeometry(QRect(40, 90, 21, 23))
        self.lightblue.setStyleSheet(u"background:rgb(82, 128, 183)")
        self.blue = QPushButton(coloredtxt)
        self.blue.setObjectName(u"blue")
        self.blue.setGeometry(QRect(70, 90, 21, 23))
        self.blue.setStyleSheet(u"background: rgb(75, 105, 255)")
        self.red = QPushButton(coloredtxt)
        self.red.setObjectName(u"red")
        self.red.setGeometry(QRect(100, 90, 21, 23))
        self.red.setStyleSheet(u"background:rgb(255, 0, 0)")
        self.lightgreen = QPushButton(coloredtxt)
        self.lightgreen.setObjectName(u"lightgreen")
        self.lightgreen.setGeometry(QRect(160, 90, 21, 23))
        self.lightgreen.setStyleSheet(u"background:rgb(170, 227, 127)")
        self.gold = QPushButton(coloredtxt)
        self.gold.setObjectName(u"gold")
        self.gold.setGeometry(QRect(130, 90, 21, 23))
        self.gold.setStyleSheet(u"background:rgb(228, 174, 57)")
        self.lime = QPushButton(coloredtxt)
        self.lime.setObjectName(u"lime")
        self.lime.setGeometry(QRect(220, 90, 21, 23))
        self.lime.setStyleSheet(u"background:rgb(162, 255, 71)")
        self.orchid = QPushButton(coloredtxt)
        self.orchid.setObjectName(u"orchid")
        self.orchid.setGeometry(QRect(250, 90, 21, 23))
        self.orchid.setStyleSheet(u"background:rgb(211, 44, 230)")
        self.lightred = QPushButton(coloredtxt)
        self.lightred.setObjectName(u"lightred")
        self.lightred.setGeometry(QRect(190, 90, 21, 23))
        self.lightred.setStyleSheet(u"background:rgb(235, 75, 75)")
        self.clear = QPushButton(coloredtxt)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(330, 90, 41, 23))
        self.send = QPushButton(coloredtxt)
        self.send.setObjectName(u"send")
        self.send.setGeometry(QRect(380, 90, 41, 23))
        self.label = QLabel(coloredtxt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 92, 41, 21))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(coloredtxt)

        QMetaObject.connectSlotsByName(coloredtxt)
    # setupUi

    def retranslateUi(self, coloredtxt):
        coloredtxt.setWindowTitle(QCoreApplication.translate("coloredtxt", u"CS:GO Colored TEXT by cl0vvn_", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("coloredtxt", u"", None))
        self.Green.setText("")
        self.lightblue.setText("")
        self.blue.setText("")
        self.red.setText("")
        self.lightgreen.setText("")
        self.gold.setText("")
        self.lime.setText("")
        self.orchid.setText("")
        self.lightred.setText("")
        self.clear.setText(QCoreApplication.translate("coloredtxt", u"Clear", None))
        self.send.setText(QCoreApplication.translate("coloredtxt", u"Send", None))
        self.label.setText(QCoreApplication.translate("coloredtxt", u"0 / 61", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    coloredtxt = QWidget()
    ui = Ui_coloredtxt()
    ui.setupUi(coloredtxt)
    coloredtxt.show()

    def green():
        #a = "[green]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def lightblue():
        #a = "[lightblu]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def blu():
        #a = "[blu]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def red():
        #a = "[red]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def lightgreen():
        #a = "[lightgreen]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def gold():
        #a = "[gold]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def lime():
        #a = "[lime]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def orchid():
        #a = "[orchid]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def lightred():
        #a = "[lightred]"
        a = ""
        ui.plainTextEdit.insertPlainText(a)
    def send():
        print(ui.plainTextEdit.toPlainText())
        text = str(ui.plainTextEdit.toPlainText())
        #text.replace("[green]", colors["green"])
        #text.replace("[lightblu]", "")
        #text.replace("[blu]", "")
        #text.replace("[red]", "")
        #text.replace("[lightgreen]", "")
        #text.replace("[gold]", "")
        ##text.replace("[lime]", "")
        #text.replace("[orchid]", "")
        #text.replace("[lightred]", "")

        run('playerchatwheel . \"{}"'.format(text))
        print(str(text))
    def clear():
        ui.plainTextEdit.clear()
    def counter():
        c = ui.plainTextEdit.toPlainText()
        clen = len(c)
        print(c)
        ui.label.setText(str(clen)+'/61')



    
    ui.Green.clicked.connect(green)
    ui.lightblue.clicked.connect(lightblue)
    ui.blue.clicked.connect(blu)
    ui.red.clicked.connect(red)
    ui.lightgreen.clicked.connect(lightgreen)
    ui.gold.clicked.connect(gold)
    ui.lime.clicked.connect(lime)
    ui.orchid.clicked.connect(orchid)
    ui.lightred.clicked.connect(lightred)

    ui.send.clicked.connect(send)
    ui.clear.clicked.connect(clear)
    ui.plainTextEdit.textChanged.connect(counter)

    sys.exit(app.exec_())

    #61