class HelloWorld(object):
	def __init__(self, *args):
		pass

	def __accept_API__(self, API):
		self.API = API

	def run(self):
		print self.API.get_plugins(True)
		print self.API.plugin_exists("Pizza!")