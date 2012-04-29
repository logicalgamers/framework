from PyQt4 import QtGui
import sys

class Basic():
	def __init__(self):
		pass

	def __accept_API__(self, API):
		self.API = API
		self.Gaia = self.API.get_plugin('Gaia')

	def run(self):
		self.gui = QtGui.QWidget()
		self.gui.setGeometry(400, 300, 210, 30)
		self.gui.setWindowTitle("Gaia Gold Getter") 

		self.Layout_Horiz_1 = QtGui.QBoxLayout(2, self.gui)

		if(self.Gaia.LoggedIn == False):
			self.API.run_plugin("GaiaLogin")
		else:
			self.GoldLabel = QtGui.QLabel(str(self.Gaia.getUsername()) + "'s Gold: ")
			self.Layout_Horiz_1.addWidget(self.GoldLabel)
			self.gui.show()