class PluginAPI():
	def __init__(self, PluginFramework):
		self.PluginFramework = PluginFramework


	#1#<-- Comment Pair Identifier. Find the other #1 and that will end what the comment below belongs to.
	###
	###	BEGIN PLUGINFRAMEWORK API INCLUSION
	###
	### Adding in some functions from the PluginFramework so that plugins 
	### should never have to explicitly call out PluginFramework.
	###
	###########################

	def reload_all_plugins(self):
		self.PluginFramework.reload_all_plugins()

	def reload_plugin(self, plugin_name):
		self.PluginFramework.reload_plugin(plugin_name)

	def get_plugins(self, namesOnly=False):
		if(not namesOnly):
			return self.PluginFramework.get_plugins()
		else:
			Plugins = self.PluginFramework.get_plugins()
			Plugins_names = []
			for Plugin in Plugins:
				Plugins_names.append(Plugin.__dict__['plugin_name'])
			return Plugins_names

	def get_plugin(self, plugin_name):
		for Plugin in self.get_plugins():
			if(Plugin.__dict__['plugin_name'] == plugin_name):
				return Plugin

	def run_plugin(self, plugin_name):
		self.get_plugin(plugin_name).run()

	def plugin_exists(self, plugin_name):
		for Plugin in self.get_plugins():
			if(Plugin.__dict__['plugin_name'] == plugin_name):
				return True
		return False

	#1#########################
	###
	###	END PLUGINFRAMEWORK API INCLUSION
	###
	###########################