from PyQt4 import QtGui, QtCore

class Plugin_ListWidget(QtGui.QListWidget):
    def __init__(self, PluginFramework_Instance, parent=None):
        super(Plugin_ListWidget, self).__init__(parent)
        self.itemDoubleClicked.connect(self.pluginDoubleClicked)
        self.Plugins = PluginFramework_Instance

    def pluginDoubleClicked(self, QListWidgetItem):
        for Plugin in self.Plugins.get_plugins():
            if(str(QListWidgetItem.text()) in str(Plugin.__dict__['plugin_name'])):
                Plugin.run()


class Gui(QtGui.QWidget):
    
    def __init__(self, PluginFramework_Instance, title="Main"):
        super(Gui, self).__init__()
        
        self.PluginFramework_Instance = PluginFramework_Instance
        self.Title = title

        self.initUI()

    def initUI(self):
        
        self.setGeometry(500, 340, 500, 340)
        self.setWindowTitle(self.Title)    

    	self.Layout = QtGui.QBoxLayout(2, self)
    	self.Plugins_ListWidget = Plugin_ListWidget(PluginFramework_Instance=self.PluginFramework_Instance) ## Create the custom QListWidget
    	self.Layout.addWidget(self.Plugins_ListWidget) ## Add the Plugins_ListWidget to the Layout.

        self.show()
