# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'produtosHtSQgz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(445, 318)
        Dialog.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 280, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(320, 10, 181, 24))
        self.checkBox1 = QCheckBox(Dialog)
        self.checkBox1.setObjectName(u"checkBox1")
        self.checkBox1.setGeometry(QRect(20, 30, 121, 20))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 60, 75, 20))
        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 90, 111, 20))
        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 180, 101, 20))
        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 120, 111, 16))
        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(20, 150, 75, 20))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(160, 30, 42, 22))
        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(160, 60, 42, 22))
        self.spinBox_3 = QSpinBox(Dialog)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(160, 90, 42, 22))
        self.spinBox_4 = QSpinBox(Dialog)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(160, 120, 42, 22))
        self.spinBox_5 = QSpinBox(Dialog)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(160, 150, 42, 22))
        self.spinBox_6 = QSpinBox(Dialog)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(160, 180, 42, 22))
        self.spinBox_7 = QSpinBox(Dialog)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(160, 210, 42, 22))
        self.checkBox_7 = QCheckBox(Dialog)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(20, 210, 101, 20))
        self.checkBox_8 = QCheckBox(Dialog)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(20, 240, 101, 20))
        self.spinBox_8 = QSpinBox(Dialog)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setGeometry(QRect(160, 240, 42, 22))
        self.webEngineView = QWebEngineView(Dialog)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(20, 280, 171, 21))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.checkBox_2.raise_()
        self.buttonBox.raise_()
        self.checkBox.raise_()
        self.checkBox.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.spinBox.raise_()
        self.spinBox_2.raise_()
        self.spinBox_3.raise_()
        self.spinBox_4.raise_()
        self.spinBox_5.raise_()
        self.spinBox_6.raise_()
        self.spinBox_7.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.spinBox_8.raise_()
        self.webEngineView.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Selecionar todos", None))
        self.checkBox1.setText(QCoreApplication.translate("Dialog", u"Coca-cola 1L", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Skol Lata", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Crystal", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"Kro-Presunto", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"Coca-cola 2L", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"Cigarro", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"Kro-Cebola", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"Skol Profissa", None))
    # retranslateUi

