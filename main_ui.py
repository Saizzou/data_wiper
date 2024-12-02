# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDzSuqt.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(335, 292)
        Dialog.setMinimumSize(QSize(324, 167))
        Dialog.setMaximumSize(QSize(600, 500))
        Dialog.setWindowIcon(QIcon("icon.ico"))
        Dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.btn_Loeschen = QPushButton(Dialog)
        self.btn_Loeschen.setObjectName(u"btn_Loeschen")
        self.btn_Loeschen.setGeometry(QRect(130, 100, 75, 24))
        self.btn_exit = QPushButton(Dialog)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(220, 100, 75, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 271, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 371, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 260, 181, 16))
        self.line_Auswahl = QLineEdit(Dialog)
        self.line_Auswahl.setObjectName(u"line_Auswahl")
        self.line_Auswahl.setGeometry(QRect(10, 70, 201, 21))
        self.btn_Auswahl = QPushButton(Dialog)
        self.btn_Auswahl.setObjectName(u"btn_Auswahl")
        self.btn_Auswahl.setGeometry(QRect(220, 70, 75, 24))
        self.text_Status = QPlainTextEdit(Dialog)
        self.text_Status.setObjectName(u"text_Status")
        self.text_Status.setGeometry(QRect(10, 130, 291, 121))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"DATA Wiper", None))
        self.btn_Loeschen.setText(QCoreApplication.translate("Dialog", u"L\u00f6schen", None))
        self.btn_exit.setText(QCoreApplication.translate("Dialog", u"Schliessen", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"DATA Wiper", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"USB Ausw\u00e4hlen:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Made by: M.Pikulski", None))
        self.btn_Auswahl.setText(QCoreApplication.translate("Dialog", u"Ausw\u00e4hlen", None))
    # retranslateUi

