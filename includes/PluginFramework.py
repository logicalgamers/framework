import sys
import fnmatch
import os
import imp
import inspect
import threading
import time

import PluginAPI

class PluginThread(threading.Thread):
    """docstring for PluginThread"""


    def __init__(self, target=None):
        threading.Thread.__init__(self, target=target)
        self.stop_event = threading.Event()
        self.__target = target

    def run(self):
        while not self.stop_event.isSet():
            self.__target()

    def stop(self):
        self.stop_event.set()

    def get_plugin_instance(self):
        return self.__target

class PluginFramework():


    def __init__(self, Plugin_Directory="./Plugins/", Plugin_Extension="*.plugin.py"):

        self.Plugin_API = PluginAPI.PluginAPI(self)
        self.Plugin_Directory = Plugin_Directory
        self.Plugin_Extension = str(Plugin_Extension)

        for root, dirs, files in os.walk(self.Plugin_Directory):  ## Append all the import directory's so that plugins can import.
            sys.path.append(root)

        self.Plugins = []
        self._load_plugins()

    def _load_plugins(self):     
        for root, dirs, files in os.walk(self.Plugin_Directory):  
            for filename in fnmatch.filter(files, self.Plugin_Extension):
                Plugin_File_Location = os.path.join(root, filename)
                name = filename.split('.')[0]
                self.Plugins.append(self._load_new_plugin(name, Plugin_File_Location))   

        for Plugin in self.Plugins: ## Give out the API instance to each plugin and start up each thread.
            #print dir(Plugin.get_plugin_instance())
            if('_accept_API' in dir(Plugin.get_plugin_instance())):
                Plugin.get_plugin_instance()._accept_API(self.Plugin_API)
            Plugin.start()

    def _load_new_plugin(self, name, plugin_location):
        Plugin = imp.load_source(name, plugin_location)
        try:
            plugin_name = name
            plugin_classname = name
            try:
                Plugin_class = Plugin.__dict__[Plugin.__name__]() # Default to the file name minus the .plugin.py
            except:
                Plugin_class = Plugin.__dict__['Plugin']() # If it can't find the file name class, it reverts to a class named Plugin, else, it drops.
                plugin_classname = 'Plugin'

            setattr(Plugin_class, "plugin_location", plugin_location)
            setattr(Plugin_class, "plugin_name", plugin_name)
            setattr(Plugin_class, "plugin_classname", plugin_classname)

            Plugin_thread = PluginThread(target=Plugin_class)
            return Plugin_thread
        except Exception, ex:
            #if(str(ex) == "'Plugin'"):
            #    print "ERROR: Class could not be located in plugin '" + str(Plugin.__name__) + "'"
            #else:
            print ex

    def reload_all_plugins(self):
        self.Plugins = []
        self._load_plugins()
        
    def reload_plugin(self, plugin_name):
        x = 0
        for Plugin in self.Plugins:
            if(Plugin.__dict__['plugin_name'] == plugin_name):
                self.Plugins[x] = self._load_new_plugin(plugin_name, Plugin.__dict__['plugin_location'])
            x+=1

    def get_plugins(self):
        return self.Plugins