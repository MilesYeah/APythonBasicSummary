

class MyProperty(object):
    def __init__(self):
        self._name = "N/A"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

o = MyProperty()
print(o.name)
o.name = "Robert"
print(o.name)
del o.name
# print(o.name)
