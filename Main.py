from includes import PluginFramework

class Main:
    def __init__(self):
        self.plugins = PluginFramework.PluginFramework()
        while(True):
            pass

if(__name__ == "__main__"):
    print("Starting up..")
    Main = Main()
    print("Exiting..")
