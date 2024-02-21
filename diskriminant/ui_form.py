# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_anaSayfa(object):
    def setupUi(self, anaSayfa):
        if not anaSayfa.objectName():
            anaSayfa.setObjectName(u"anaSayfa")
        anaSayfa.resize(419, 367)
        self.label = QLabel(anaSayfa)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 151, 101))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(anaSayfa)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 16, 21))
        self.layoutWidget = QWidget(anaSayfa)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 140, 131, 86))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_A = QLineEdit(self.layoutWidget)
        self.lineEdit_A.setObjectName(u"lineEdit_A")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_A)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_B = QLineEdit(self.layoutWidget)
        self.lineEdit_B.setObjectName(u"lineEdit_B")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_B)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_C = QLineEdit(self.layoutWidget)
        self.lineEdit_C.setObjectName(u"lineEdit_C")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_C)

        self.pushButton = QPushButton(anaSayfa)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 140, 81, 81))
        self.label_x1 = QLabel(anaSayfa)
        self.label_x1.setObjectName(u"label_x1")
        self.label_x1.setGeometry(QRect(30, 270, 71, 21))
        self.label_x2 = QLabel(anaSayfa)
        self.label_x2.setObjectName(u"label_x2")
        self.label_x2.setGeometry(QRect(170, 270, 71, 21))
        self.label_8 = QLabel(anaSayfa)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 280, 16, 21))
        self.label_9 = QLabel(anaSayfa)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 280, 16, 21))

        self.retranslateUi(anaSayfa)

        QMetaObject.connectSlotsByName(anaSayfa)
    # setupUi

    def retranslateUi(self, anaSayfa):
        anaSayfa.setWindowTitle(QCoreApplication.translate("anaSayfa", u"anaSayfa", None))
        self.label.setText(QCoreApplication.translate("anaSayfa", u"ax+bx+c = 0", None))
        self.label_2.setText(QCoreApplication.translate("anaSayfa", u"2", None))
        self.label_3.setText(QCoreApplication.translate("anaSayfa", u"a=", None))
        self.label_4.setText(QCoreApplication.translate("anaSayfa", u"b=", None))
        self.label_5.setText(QCoreApplication.translate("anaSayfa", u"c=", None))
        self.pushButton.setText(QCoreApplication.translate("anaSayfa", u"HESAPLA", None))
        self.label_x1.setText(QCoreApplication.translate("anaSayfa", u"X   = ", None))
        self.label_x2.setText(QCoreApplication.translate("anaSayfa", u"X  = ", None))
        self.label_8.setText(QCoreApplication.translate("anaSayfa", u"1", None))
        self.label_9.setText(QCoreApplication.translate("anaSayfa", u"2", None))
    # retranslateUi

