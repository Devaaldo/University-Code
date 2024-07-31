# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 331)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_transaction = QFrame(Dialog)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setFrameShape(QFrame.NoFrame)
        self.new_transaction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.new_transaction)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_new_transaction = QLabel(self.new_transaction)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.lbl_new_transaction)

        self.cb_choose_category = QComboBox(self.new_transaction)
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.setObjectName(u"cb_choose_category")

        self.verticalLayout_21.addWidget(self.cb_choose_category)

        self.dateEdit = QDateEdit(self.new_transaction)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 6, 13), QTime(0, 0, 0)))
        self.dateEdit.setCurrentSectionIndex(0)

        self.verticalLayout_21.addWidget(self.dateEdit)

        self.le_description = QLineEdit(self.new_transaction)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.new_transaction)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.le_balance)

        self.cb_status = QComboBox(self.new_transaction)
        self.cb_status.addItem("")
        self.cb_status.addItem("")
        self.cb_status.setObjectName(u"cb_status")

        self.verticalLayout_21.addWidget(self.cb_status)

        self.btn_new_transaction = QPushButton(self.new_transaction)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout_21.addWidget(self.btn_new_transaction)


        self.verticalLayout.addWidget(self.new_transaction)


        self.retranslateUi(Dialog)

        self.cb_choose_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"Transaksi Baru", None))
        self.cb_choose_category.setItemText(0, QCoreApplication.translate("Dialog", u"Work", None))
        self.cb_choose_category.setItemText(1, QCoreApplication.translate("Dialog", u"Auto", None))
        self.cb_choose_category.setItemText(2, QCoreApplication.translate("Dialog", u"Other", None))
        self.cb_choose_category.setItemText(3, QCoreApplication.translate("Dialog", u"Grocery", None))
        self.cb_choose_category.setItemText(4, QCoreApplication.translate("Dialog", u"Entertainment", None))

        self.cb_choose_category.setProperty("placeholderText", QCoreApplication.translate("Dialog", u"Choose category", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"d/M/yyyy", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb_status.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb_status.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.cb_status.setProperty("placeholderText", QCoreApplication.translate("Dialog", u"Choose status", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Simpan Transaksi", None))
    # retranslateUi

