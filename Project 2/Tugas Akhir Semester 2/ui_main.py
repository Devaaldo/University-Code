# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 673)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balances_frame = QFrame(self.centralwidget)
        self.balances_frame.setObjectName(u"balances_frame")
        self.balances_frame.setFrameShape(QFrame.NoFrame)
        self.balances_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.balances_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_current_balance = QLabel(self.balances_frame)
        self.lbl_current_balance.setObjectName(u"lbl_current_balance")

        self.verticalLayout_21.addWidget(self.lbl_current_balance)

        self.current_balance = QLabel(self.balances_frame)
        self.current_balance.setObjectName(u"current_balance")
        self.current_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.current_balance)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_income = QLabel(self.balances_frame)
        self.lbl_income.setObjectName(u"lbl_income")

        self.horizontalLayout_9.addWidget(self.lbl_income)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.income_balance = QLabel(self.balances_frame)
        self.income_balance.setObjectName(u"income_balance")
        self.income_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.income_balance)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_outcome = QLabel(self.balances_frame)
        self.lbl_outcome.setObjectName(u"lbl_outcome")

        self.horizontalLayout_10.addWidget(self.lbl_outcome)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.outcome_balance = QLabel(self.balances_frame)
        self.outcome_balance.setObjectName(u"outcome_balance")
        self.outcome_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.outcome_balance)


        self.horizontalLayout_2.addWidget(self.balances_frame)

        self.balances_frame_2 = QFrame(self.centralwidget)
        self.balances_frame_2.setObjectName(u"balances_frame_2")
        self.balances_frame_2.setFrameShape(QFrame.NoFrame)
        self.balances_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.balances_frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.lbl_expenses_categories = QLabel(self.balances_frame_2)
        self.lbl_expenses_categories.setObjectName(u"lbl_expenses_categories")

        self.verticalLayout_20.addWidget(self.lbl_expenses_categories)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_groceries = QLabel(self.balances_frame_2)
        self.lbl_groceries.setObjectName(u"lbl_groceries")

        self.horizontalLayout_3.addWidget(self.lbl_groceries)

        self.total_groceries = QLabel(self.balances_frame_2)
        self.total_groceries.setObjectName(u"total_groceries")
        self.total_groceries.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.total_groceries)


        self.verticalLayout_20.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_entertainment = QLabel(self.balances_frame_2)
        self.lbl_entertainment.setObjectName(u"lbl_entertainment")

        self.horizontalLayout_4.addWidget(self.lbl_entertainment)

        self.total_entertainment = QLabel(self.balances_frame_2)
        self.total_entertainment.setObjectName(u"total_entertainment")
        self.total_entertainment.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.total_entertainment)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_auto = QLabel(self.balances_frame_2)
        self.lbl_auto.setObjectName(u"lbl_auto")

        self.horizontalLayout_5.addWidget(self.lbl_auto)

        self.total_auto = QLabel(self.balances_frame_2)
        self.total_auto.setObjectName(u"total_auto")
        self.total_auto.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.total_auto)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_other = QLabel(self.balances_frame_2)
        self.lbl_other.setObjectName(u"lbl_other")

        self.horizontalLayout_6.addWidget(self.lbl_other)

        self.total_other = QLabel(self.balances_frame_2)
        self.total_other.setObjectName(u"total_other")
        self.total_other.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.total_other)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addWidget(self.balances_frame_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_transaction = QPushButton(self.btn_frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_new_transaction)

        self.btn_delete_transaction = QPushButton(self.btn_frame)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setMinimumSize(QSize(230, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_transaction.setIcon(icon)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_transaction)

        self.btn_edit_transaction = QPushButton(self.btn_frame)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setMinimumSize(QSize(230, 50))
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_edit_transaction)


        self.verticalLayout_2.addWidget(self.btn_frame)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(155)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance/Saldo Saat ini", None))
        self.current_balance.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_income.setText(QCoreApplication.translate("MainWindow", u"Income/Pemasukan", None))
        self.income_balance.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome/Pengeluaran", None))
        self.outcome_balance.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_expenses_categories.setText(QCoreApplication.translate("MainWindow", u"Categories/Kategori", None))
        self.lbl_groceries.setText(QCoreApplication.translate("MainWindow", u"Belanja", None))
        self.total_groceries.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_entertainment.setText(QCoreApplication.translate("MainWindow", u"Hiburan", None))
        self.total_entertainment.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_auto.setText(QCoreApplication.translate("MainWindow", u"Cicilan", None))
        self.total_auto.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.lbl_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.total_other.setText(QCoreApplication.translate("MainWindow", u"Rp12000", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
    # retranslateUi

