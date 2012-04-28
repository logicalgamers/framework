import string

class Custom():
	def run(self):
		HTTP = HTTPWrapper()
		URL = raw_input("HTTP Req URL: ")
		Type = raw_input("HTTP Req Type( (P)ost or (G)et ): ")
		if(string.lower(Type[0]) == "p"):
			Count = int(raw_input("HTTP Post Data Count: "))
			PostData = {}
			for x in xrange(0, Count):
				Name = raw_input("(" + str(x) + ") Name: ")
				Value = raw_input("(" + str(x) + ") Value: ")
				PostData[Name] = Value
		else:
			PostData = None
		print HTTP.Post(URL, PostData)

import urllib
import urllib2
import cookielib
class HTTPWrapper():
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