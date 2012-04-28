from PyQt4 import QtGui
import sys
from Gaia import Gaia

class Basic():
	def __init__(self):
		self.Gaia = Gaia()

	def __accept_API__(self, API):
		self.API = API

	def run(self):
		print "Basic Gaia Application starting up.."
		self.gui = QtGui.QWidget()
		self.gui.setGeometry(400, 300, 400, 300)
		self.gui.setWindowTitle("Basic Gaia+GUI Plugin") 

		self.gui.show()