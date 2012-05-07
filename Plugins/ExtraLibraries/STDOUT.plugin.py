import sys
import time
import inspect

class STDOUT():
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
    	if(data != "\n" and data != ""):
    		Time = time.time()
    		if(len(str(Time)) == 12):  ## Do this to keep the length of the time always the same.
    			Time = str(Time) + "0"
    		self.write_color(Time, 'bright blue')
    		frm = inspect.stack()[1]
    		try:
    			Name_spl = str(frm[1]).split('/')
    			plugin_name = Name_spl[len(Name_spl)-1].split('.')[0]
    		except: 
    			plugin_name = "Unknown"

    		self.write_color(plugin_name, 'bright green')
        self.stream.write(data)
        self.stream.flush()

    def write_color(self, data, color):
    	Colors = {'black':    '0;30',     'bright gray':  '0;37',
	    'blue':     '0;34',     'white':        '1;37',
	    'green':    '0;32',     'bright blue':  '1;34',
	    'cyan':     '0;36',     'bright green': '1;32',
	    'red':      '0;31',     'bright cyan':  '1;36',
	    'purple':   '0;35',     'bright red':   '1;31',
	    'yellow':   '0;33',     'bright purple':'1;35',
	    'dark gray':'1;30',     'bright yellow':'1;33',
	    'normal':   '0'}
    	self.stream.write("\033[" + Colors[color] + "m" + str(data) + ": \033[0m")

    def __getattr__(self, attr):
        return getattr(self.stream, attr)
sys.stdout=STDOUT(sys.stdout)