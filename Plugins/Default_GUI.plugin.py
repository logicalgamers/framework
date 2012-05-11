from PyQt4 import QtGui, QtCore

class Default_GUI():
    def __init__(self):
        pass

    def _accept_API(self, API):
        self.GUI = GUI(API)
        
class Plugin_ListWidget(QtGui.QListWidget):
    def __init__(self, API, parent=None):
        super(Plugin_ListWidget, self).__init__(parent)
        self.itemDoubleClicked.connect(self.pluginDoubleClicked)
        self.Plugins_API = API

    def plugin_double_clicked(self, QListWidgetItem):
        for Plugin in self.Plugins_API.get_plugins():
            if(str(QListWidgetItem.text()) in str(Plugin.__dict__['plugin_name'])):
                Plugin.run()

class GUI(QtGui.QWidget):
    
    def __init__(self, API, title="Main"):
        super(GUI, self).__init__()
        
        self.API = API
        self.Title = title

        self.initUI()

    def init_UI(self):
        
        self.setGeometry(500, 340, 500, 340)
        self.setWindowTitle(self.Title)    

        self.Layout = QtGui.QBoxLayout(2, self)
        self.Plugins_ListWidget = Plugin_ListWidget(API=self.API)   ## Create the custom QListWidget
        self.Layout.addWidget(self.Plugins_ListWidget)              ## Add the Plugins_ListWidget to the Layout.

        print self.API.plugin_exists("Custom")
        for Plugin in self.API.get_plugins():
            if(Plugin != None):                                                 ## Just to make sure that the plugin was loaded 
                if('plugin_name' in Plugin.__dict__ and 'run' in dir(Plugin)):  ## correctly and all that before we add it to the ListWidget.
                    self.Plugins_ListWidget.addItem(Plugin.__dict__['plugin_name'])

        self.show()