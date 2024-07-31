import sys
from PyQt5 import QtWidgets
from login_layout import Ui_Form as login_layout
from main_layout import Ui_Form as main_layout

class DaftarBelanja(login_layout):
	def __init__(self, dialog):
		login_layout.__init__(self)
		self.setupUi(dialog)

		self.QpushButton_login.clicked.connect(self.login)
		self.QpushButton_batal.clicked.connect(self.batal)

	def login(self):
		username = self.lineEditUsername.text()
		password = self.lineEditPassword.text()
		if(username == "unjaya" and password == "unjaya"):
			self.mainWindow = QtWidgets.QDialog()
			self.mainUI = main_layout()
			self.mainUI.setupUi(self.mainWindow)
			loginWindow.hide()
			self.mainWindow.show()

		self.mainUI.QpushButton_simpan.clicked.connect(self.tambahData)
		self.mainUI.QpushButton_hapus.clicked.connect(self.hapusData)

	def tambahData(self):
		nama_barang = self.mainUI.QLineEdit_NamaBarang.text()
		banyak_barang = self.mainUI.QLineEdit_BanyakBarang.text()
		harga_barang = self.mainUI.QLineEdit_Harga.text()

		rowPosition = self.mainUI.tableWidgetData.rowCount()

		self.mainUI.tableWidgetData.insertRow(rowPosition)
		self.mainUI.tableWidgetData.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama_barang))
		self.mainUI.tableWidgetData.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(banyak_barang))
		self.mainUI.tableWidgetData.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(harga_barang))

	def hapusData(self):
		selectedRow = self.mainUI.tableWidgetData.currentRow()
		nama_barang = self.mainUI.tableWidgetData.item(selectedRow,0).text()
		self.mainUI.tableWidgetData.removeRow(selectedRow)

	def batal(self):
		app = QtWidgets.QApplication(sys.argv)
		ex = login_layout()
		sys.exit(app.exec_())
	

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	loginWindow = QtWidgets.QDialog()

	loginUI = DaftarBelanja(loginWindow)

	loginWindow.show()
	sys.exit(app.exec_())