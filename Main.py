from PyQt4 import QtGui
from includes import PluginFramework, PluginAPI, STDOUT
import sys

class Main:
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.Plugins = PluginFramework.PluginFramework()
	    
	def run(self):
		self.app.exec_()


if(__name__ == "__main__"):
	print("Starting up..")
	Main = Main()
	Main.run()
	print("Exiting..")
