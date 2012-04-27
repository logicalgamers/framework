from PyQt4 import QtGui
import sys

class Basic():
	def run(self):
		print "Basic Application starting up.."
		self.gui = QtGui.QWidget()
		self.gui.setGeometry(500, 340, 500, 340)
		self.gui.setWindowTitle("FUCKING")    

		self.gui.show()
		print "GUI SHOWN."
