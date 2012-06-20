from Tkinter import *
from threading import *
import random
import string
import time

from Pmw import *
import Pmw

TITLE = "LG Framework - www.logicalgamers.com"

class Default_GUI():


    def __init__(self):
        pass

    def _accept_API(self, API):
        self.API = API

    def __call__(self):
        root = Tk()
        root.title(TITLE)

        app = GUI(master=root, API=self.API)

        root.mainloop()

class Drop_Down_Item:
    def __init__(self, PluginThread):
        self.PT = PluginThread
        self.ID = self.id_generator()
        print "INIT"

    def __str__(self):
        return self.ID

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

class Plugin_Row:


    def __init__(self, parent, plugin_def_thread, API):

        self.parent = parent
        self.API = API

        self.plugin_threads = []

        self.plugin_def_thread = self.API.get_plugins()[plugin_def_thread][0]
        self.plugin_instance = self.plugin_def_thread.get_plugin_instance()

        self.plugin_name = self.plugin_instance.__dict__['plugin_name']
        print self.plugin_name

        self.plugin_threads.append(self.plugin_def_thread)

        self.frame = Frame(parent, relief=SOLID, bd=1)
        self.frame.pack(side=TOP,expand=True, fill=BOTH,pady=10,anchor="c")
        
        pluginFrame = Frame(self.frame, relief=SUNKEN, bd=1)
        pluginFrame.pack(side=BOTTOM, anchor="e", fill=X, expand=True)

        groupFrame = Frame(pluginFrame)
        groupFrame.pack(side=BOTTOM, anchor=W, expand=True)

        label = Label(groupFrame, text=self.plugin_instance.__dict__['plugin_name'], justify=LEFT, anchor="w", bg = "#5050b0")
        label.pack(side=LEFT)

        self.drop_down_items = []
        for item in self.get_all_instances():
            self.drop_down_items.append(Drop_Down_Item(item))

        self.drop_down = Pmw.OptionMenu(groupFrame, items=self.drop_down_items)
        self.drop_down.pack(side=LEFT)

        self.run = Button(groupFrame, text="Run", command=self.run_new_instance, width=3)
        self.run.pack(side=LEFT) 

        self.kill_selected = Button(groupFrame, text="Kill", command=self.kill_selected_thread, width=3)
        self.kill_selected.pack(side=LEFT)  

    def kill_selected_thread(self):
        selected = self.get_thread_from_DDI_id(self.drop_down.getcurselection())
        self.remove_thread_from_DDI_id(self.drop_down.getcurselection())
        selected.PT.stop()
        self.update_drop_down()

    def remove_thread_from_DDI_id(self, DDI_id):
        for item in self.drop_down_items:
            if(item.ID == DDI_id):
                self.drop_down_items.remove(item)
            time.sleep(0.001)

    def get_thread_from_DDI_id(self, DDI_id):
        for item in self.drop_down_items:
            if(item.ID == DDI_id):
                return item
            time.sleep(0.001)

    def run_new_instance(self):
        new_instance = self.API.create_new_instance(self.plugin_def_thread.get_plugin_instance().__dict__['plugin_name'])
        new_instance.start()
        print "New Instance of " + str(self.plugin_def_thread.get_plugin_instance().__dict__['plugin_name']) + " created.."
        self.update_drop_down()

    def update_drop_down(self):
        # Update the drop down menu with all instances.        
        self.drop_down_items = []
        for item in self.get_all_instances():
            self.drop_down_items.append(Drop_Down_Item(item))

        self.drop_down.setitems(self.drop_down_items)
        self.drop_down.update()

    def get_all_instances(self):
        return self.API.get_plugins()[self.plugin_name]


class GUI(Frame):
    

    def __init__(self, master, API):

        Frame.__init__(self, master)
        self.API = API

        self.master = master
        self.master.protocol('WM_DELETE_WINDOW', self.delete_window)

        menubar = Frame(self.master)
        menubar.pack(side=TOP, fill=X)

        fileMenuButton = Menubutton(menubar, text='Program', underline=0)
        fileMenuButton.pack(side=LEFT)
        fileMenu = Menu(fileMenuButton, tearoff=0)
        fileMenuButton.config(menu=fileMenu)

        fileMenu.add_cascade(label="List Instances", command=self.list_instances)

        self.sf = Pmw.ScrolledFrame(self.master, horizflex='expand', usehullsize=1, hull_width=500, hull_height=350)
        self.sf.pack(fill=BOTH,expand=True, anchor="w")

        self.pluginFrame = self.sf.interior()

        self.Rows = []

        for plugin_name in self.API.get_plugins():
            try:
                plugin = self.API.get_plugins()[plugin_name][0]

                if('run' in dir(plugin.get_plugin_instance())):
                    self.Rows.append(Plugin_Row(self.pluginFrame, plugin_name, self.API))
            except Exception, ex:
                print ex
            time.sleep(0.001)

    def delete_window(self):
        self.master.destroy()
        print "Default_GUI has been destroyed."

    def list_instances(self):

        for Row in self.Rows:
            print Row.plugin_name + " : " + str(Row.get_all_instances())
            time.sleep(0.001)