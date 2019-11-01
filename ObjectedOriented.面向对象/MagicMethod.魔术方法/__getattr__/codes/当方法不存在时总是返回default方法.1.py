
class Test(object):
    def __init__(self):
        print("A class, when calling a undefined method, the default_method will be called.")
    
    def __getattr__(self, attr):
        return self.default_method

    def default_method(self):
        print("Execute default_method.")
    
o = Test()
o.f1()
o.f2()
o.f3()
