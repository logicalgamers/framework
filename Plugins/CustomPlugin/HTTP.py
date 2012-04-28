import urllib
import urllib2
import cookielib

class HTTP():
	def __init__(self):
		self.cookiejar = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookiejar))

	def Get(self, url):
		return self._req(url)

	def Post(self, url, data):
		return self._req(url, data)

	def _req(self, url, data=None):
		if(data != None):
			if(not isinstance(data, str)):
				data = ""
		return self.opener.open(url, data).read()