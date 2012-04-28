import string
from HTTP import HTTP as HTTPWrapper

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
