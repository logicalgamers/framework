from General import General

class Gaia():
	def __init__(self, Username=None, Password=None, HTTPWrapper=None):
		self.Username = Username
		self.Password = Password
		if(HTTPWrapper == None):
			from HTTP import HTTP as HTTPWrapper
			self.HTTP = HTTPWrapper()
		else:
			self.HTTP = HTTPWrapper
		self.HTTP.setHeader('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0')
		self.General = General()
		self.LoggedIn = False

	def login(self, Username=None, Password=None):
		if(self.LoggedIn == True):
			return True

		if(Username == None):
			if(self.Username == None):
				return False
			else:
				Username = self.Username
		else:
			self.Username = Username

		if(Password == None):
			if(self.Password == None):
				return False
			else:
				Password = self.Password
		else:
			self.Password = Password

		print 'Attempting Gaia login..'
		params = dict()
		Req = self.HTTP.Get(GaiaConstants.URL_LOGIN_DEFAULT)

		Req = Req.replace("\t", " ").replace("\n", "").replace("    ", " ").replace('data-value', 'data')
		data = self.General.getBetween(Req, '<form action="/auth/login/" id="memberloginForm" method="post">', '</form>')

		for x in xrange(0, data.count('input')-1):                     ### Due to randomization of the order, and a hidden value that has a random name/value,
																	   ### I am just building post data automatically. Then modify user/pass later.
			complete = self.General.getBetween(data, '<input', '/>')
			name = self.General.getBetween(complete, 'name="', '"')
			value = self.General.getBetween(complete, 'value="', '"')
			params[name] = value
			try:
				data = data.split(complete)[1]
			except:
				pass

		params['username'] = Username
		params['password'] = Password
		params['chap'] = ''
		params['redirect'] = 'http://www.gaiaonline.com/'
		params['signInButton'] = 'Log+In'

		Login_Req = self.HTTP.Post(GaiaConstants.URL_LOGIN_DEFAULT, params)
		if('View or change your Account Settings' in Login_Req):
			self.LoggedIn = True
			return True
		else:
			self.LoggedIn = False
			return False

	def getGold(self):
		if(self.LoggedIn == False):
			return '0'
		Req = self.HTTP.Get(GaiaConstants.URL_HOME)
		return self.General.getBetween(Req, '<span id="go1d_amt">', '</span>')

	def getUsername(self):
		return self.Username


class GaiaConstants():
	URL_HOME = "http://www.gaiaonline.com/"
	URL_LOGIN_DEFAULT = "http://www.gaiaonline.com/auth/login/"