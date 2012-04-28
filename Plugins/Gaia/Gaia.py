
class Gaia():
	def __init__(self, Username=None, Password=None, HTTPWrapper=None):
		self.Username = Username
		self.Password = Password
		if(HTTPWrapper == None):
			from HTTP import HTTP as HTTPWrapper
			self.HTTP = HTTPWrapper()
		else:
			self.HTTP = HTTPWrapper

	def login(self, Username=None, Password=None):
		if(Username == None):
			if(self.Username == None):
				return False
			else:
				Username = self.Username

		if(Password == None):
			if(self.Password == None):
				return False
			else:
				Password = self.Password

		Req = self.HTTP.Get(GaiaConstants.URL_LOGIN_DEFAULT)


class GaiaConstants():
	URL_LOGIN_DEFAULT = "http://www.gaiaonline.com/auth/login/index.php"
	DATA_LOGIN_DEFAULT = {	"username": "", 
							"password": "", 
							"signInButton": "", 
							"sid": "", 
							"token": "", 
							"redirect": "http%3A%2F%2Fwww.gaiaonline.com%2F", 
							"chap": ""}