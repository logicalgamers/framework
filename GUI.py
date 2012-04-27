from PluginFramework import *
import sys
import time
import inspect
from PyQt4 import QtGui, QtCore
from threading import Thread

class Plugin_ListWidget(QtGui.QListWidget):
	def __init__(self, parent=None):
		super(Plugin_ListWidget, self).__init__(parent)
		self.itemDoubleClicked.connect(self.pluginDoubleClicked)

	def pluginDoubleClicked(self, QListWidgetItem):
		#print QListWidgetItem.text()
		Plugins = globals()['Main'].Plugins # Back tracked to the Main class's self.Plugins
		for Plugin in Plugins.get_plugins():
			if(str(QListWidgetItem.text()) in str(Plugin.__dict__['plugin_name'])):
				Plugin.run()


class Gui(QtGui.QWidget):
    
    def __init__(self, title="Main"):
        super(Gui, self).__init__()
        
        self.Title = title

        self.initUI()

    def initUI(self):
        
        self.setGeometry(500, 340, 500, 340)
        self.setWindowTitle(self.Title)    

    	self.Layout = QtGui.QBoxLayout(2, self)
    	self.Plugins_ListWidget = Plugin_ListWidget() ## Create the custom QListWidget
    	self.Layout.addWidget(self.Plugins_ListWidget) ## Add the Plugins_ListWidget to the Layout.

        self.show()

class Main:
	def __init__(self):
		self.Plugins = PluginFramework()

		self.app = QtGui.QApplication(sys.argv)
		self.gui = Gui()
	    
	def run(self):
		for Plugin in self.Plugins.get_plugins():
			if(Plugin != None):
				if('plugin_name' in Plugin.__dict__):
					self.gui.Plugins_ListWidget.addItem(Plugin.__dict__['plugin_name'])

		#sys.exit(self.app.exec_())
		self.app.exec_()

class stdout_Unbuffered():
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
    	if(data != "\n" and data != ""):
    		Time = time.time()
    		if(len(str(Time)) == 12):  ## Do this to keep the length of the time always the same.
    			Time = str(Time) + "0"
    		self.write_color(Time, 'bright blue')
    		#self.write_color(inspect.stack()[1][1], 'bright red')
    		frm = inspect.stack()[1]
    		try:
    			Name_spl = str(frm[1]).split('/')
    			plugin_name = Name_spl[len(Name_spl)-1].split('.')[0]
    		except: 
    			plugin_name = "Unknown"

    		self.write_color(plugin_name, 'bright green')
        self.stream.write(data)
        self.stream.flush()

    def write_color(self, data, color):
    	Colors = {'black':    '0;30',     'bright gray':  '0;37',
	    'blue':     '0;34',     'white':        '1;37',
	    'green':    '0;32',     'bright blue':  '1;34',
	    'cyan':     '0;36',     'bright green': '1;32',
	    'red':      '0;31',     'bright cyan':  '1;36',
	    'purple':   '0;35',     'bright red':   '1;31',
	    'yellow':   '0;33',     'bright purple':'1;35',
	    'dark gray':'1;30',     'bright yellow':'1;33',
	    'normal':   '0'}
    	self.stream.write("\033[" + Colors[color] + "m" + str(data) + ": \033[0m")

    def __getattr__(self, attr):
        return getattr(self.stream, attr)
sys.stdout=stdout_Unbuffered(sys.stdout)


if(__name__ == "__main__"):
	print("Starting up..")
	Main = Main()
	Main.run()
	print("Exiting..")
