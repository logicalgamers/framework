from Tkinter import *
from threading import *

from Pmw import *
import Pmw

class Default_GUI():


    def __init__(self):
        pass

    def _accept_API(self, API):
        self.API = API

    def __call__(self):
        root = Tk()
        root.title("LG Framework - www.logicalgamers.com")

        app = GUI(master=root, API=self.API)

        root.mainloop()

class Plugin_Row:


    def __init__(self, parent, plugin_def_thread, API):

        self.parent = parent
        self.API = API

        self.plugin_threads = []

        #print dir(self.API.get_plugins()[plugin_def_thread][0])
        self.plugin_def_thread = self.API.get_plugins()[plugin_def_thread][0]
        self.plugin_instance = self.plugin_def_thread.get_plugin_instance()

        self.plugin_threads.append(self.plugin_def_thread)

        if('run' in dir(self.plugin_instance)):
            self.frame = Frame(parent, relief=SOLID, bd=1)
            self.frame.pack(side=TOP,expand=True, fill=BOTH,pady=10,anchor="c")
            
            pluginFrame = Frame(self.frame, relief=SUNKEN, bd=1)
            pluginFrame.pack(side=BOTTOM, anchor="e", fill=X, expand=True)

            groupFrame = Frame(pluginFrame,relief=GROOVE, bd=1)

            label = Label(groupFrame, text=self.plugin_instance.__dict__['plugin_name'], justify=LEFT, anchor="w",bg = "#5050b0")
            label.pack(side=LEFT)
                    
            self.run = Button(groupFrame, text="Run", command=self.run_new_instance)
            self.run.pack(side=RIGHT)    

            groupFrame.pack(side=BOTTOM, fill=X, expand=True)

    def run_new_instance(self):
        new_instance = self.API.create_new_instance(self.plugin_def_thread.get_plugin_instance().__dict__['plugin_name'])
        print dir(new_instance)
        print "New Instance of " + str(self.plugin_def_thread.get_plugin_instance().__dict__['plugin_name']) + " created.."

class GUI(Frame):
    

    def __init__(self, master, API):

        Frame.__init__(self, master)
        self.API = API

        menubar = Frame(master)
        menubar.pack(side=TOP, fill=X)

        fileMenuButton = Menubutton(menubar, text='Program', underline=0)
        fileMenuButton.pack(side=LEFT)
        fileMenu = Menu(fileMenuButton, tearoff=0)
        fileMenuButton.config(menu=fileMenu)

        self.sf = Pmw.ScrolledFrame(master, horizflex='expand', usehullsize=1, hull_width=500, hull_height=350)
        self.sf.pack(fill=BOTH,expand=True, anchor="w")

        self.pluginFrame = self.sf.interior()

        for plugin in self.API.get_plugins():
            Plugin_Row(self.pluginFrame, plugin, self.API)#fileMenu.add_cascade(label=self.API.get_plugin_name(plugin))
