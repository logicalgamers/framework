

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
                Plugins_names.append(self.get_plugin_name(Plugin))
            return Plugins_names
        return self.PluginFramework.get_plugins()

    def get_plugin(self, plugin_name):
        try:
            for Plugin in self.get_plugins():
                if(self.get_plugin_name(Plugin) == plugin_name):
                    return Plugin
        except Exception, ex:
            return ex

    def get_plugin_name(self, plugin_object):
        print plugin_object.get_plugin_instance().__dict__['plugin_name']
        return plugin_object.get_plugin_instance().__dict__['plugin_name']

    def run_plugin(self, plugin_name):
        self.get_plugin(plugin_name).run()

    def plugin_exists(self, plugin_name):
        for Plugin in self.get_plugins():
            if(Plugin.__dict__['plugin_name'] == plugin_name):
                return True
        return False

    def create_new_instance(self, plugin_name):
        plugin_def_instance = self.get_plugins()[plugin_name][0].get_plugin_instance()

        location = plugin_def_instance.__dict__['plugin_location']

        new_instance = self.PluginFramework._load_new_plugin(plugin_name, location)
        self.PluginFramework.Plugins[plugin_name].append(new_instance)
        return new_instance