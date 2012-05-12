

class PluginAPI():


    def __init__(self, PluginFramework):
        self.PluginFramework = PluginFramework

    def reload_all_plugins(self):
        self.PluginFramework.reload_all_plugins()

    def reload_plugin(self, plugin_name):
        self.PluginFramework.reload_plugin(plugin_name)

    def get_plugins(self, namesOnly=False):
        if namesOnly:
            Plugins = self.PluginFramework.get_plugins()
            Plugins_names = []
            for Plugin in Plugins:
                Plugins_names.append(Plugin.__dict__['plugin_name'])
            return Plugins_names
        return self.PluginFramework.get_plugins()

    def get_plugin(self, plugin_name):
        try:
            for Plugin in self.get_plugins():
                if(Plugin.__dict__['plugin_name'] == plugin_name):
                    return Plugin
        except Exception, ex:
            return ex

    def run_plugin(self, plugin_name):
        self.get_plugin(plugin_name).run()

    def plugin_exists(self, plugin_name):
        for Plugin in self.get_plugins():
            if(Plugin.__dict__['plugin_name'] == plugin_name):
                return True
        return False