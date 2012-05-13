
class Test_Threading():
    def __init__(self):
        print "Test_Threading init"

    def run(self):
        while(True):
            print "Test_Threading"

    def __call__(self):
        print "Test_Threading __call__"
        self.run()