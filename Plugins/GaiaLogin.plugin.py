from PyQt4 import QtGui
import sys

class GaiaLogin():
	def __accept_API__(self, API):
		self.API = API
		self.Gaia = self.API.get_plugin('Gaia')

	def Login_PushButton_clicked(self, *args):
		Username=str(self.Username_LineEdit.text())
		Password=str(self.Password_LineEdit.text())
		if(self.Gaia.login(Username, Password)):
			self.gui.hide()
			print "Logged in!"
		else:
			print "Login failed.."

	def run(self):
		self.gui = QtGui.QWidget()
		self.gui.setGeometry(400, 300, 210, 110)
		self.gui.setWindowTitle("Gaia Login") 

		self.Layout_Horiz_1 = QtGui.QBoxLayout(2, self.gui)

		self.Username_LineEdit = QtGui.QLineEdit("IDestroyYou_K")
		self.Layout_Horiz_1.addWidget(self.Username_LineEdit) 

		self.Password_LineEdit = QtGui.QLineEdit("Password")
		self.Password_LineEdit.setEchoMode(2)
		self.Layout_Horiz_1.addWidget(self.Password_LineEdit)

		self.Login_PushButton = QtGui.QPushButton("Login")
		self.Login_PushButton.clicked.connect(self.Login_PushButton_clicked)
		self.Layout_Horiz_1.addWidget(self.Login_PushButton) 

		self.gui.show()