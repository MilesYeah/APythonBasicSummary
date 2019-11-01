
class MyName(object):
    def __init__(self):
        self._name = "N/A"

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name)


o = MyName()
print(o.name)
o.name = "Robert"
print(o.name)
del o.name
# print(o.name)
