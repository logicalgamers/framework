from PyQt4 import QtGui
import sys

class Basic():
	def __init__(self, *args):
		pass

	def __accept_API__(self, API):
		self.API = API
		print "Accepted the API"

	def run(self):
		print "Basic Application starting up.."
		self.gui = QtGui.QWidget()
		self.gui.setGeometry(400, 300, 400, 300)
		self.gui.setWindowTitle("Basic GUI Plugin")    

		self.API.run_plugin("HelloWorld")

		self.gui.show()
		print "GUI SHOWN."