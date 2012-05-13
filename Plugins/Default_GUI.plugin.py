from Tkinter import *

class Default_GUI():


    def __init__(self):
        pass

    def _accept_API(self, API):
        self.API = API

    def __call__(self):
        root = Tk()
        self.GUI = GUI(self.API, master=root)
        self.GUI.mainloop()

class GUI(Frame):
    

    def __init__(self, API, title="Main", master=None):

        Frame.__init__(self, master)
        
        self.API = API
        self.Title = title

        self.grid()
        self.createWidgets()

        self.master.title(self.Title)

    def createWidgets(self):
        self.quitButton = Button(self, text="Quit", command=self.quit_)
        self.quitButton.grid()

    def quit_(self):
        self.destroy()
        quit()
