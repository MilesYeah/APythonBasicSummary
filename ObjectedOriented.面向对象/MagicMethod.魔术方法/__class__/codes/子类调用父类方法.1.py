
class A(object):
    num = 10
    def __init__(self):
        print("init A")

    def method(self):
        print("method a")

class B(A):
    num=20
    def __init__(self):
        print("init B")

    def method(self):
        print("method b")


o1 = A()
o1.method()

o2 = B()
o2.method()

print("-" * 10)
print(o1.num, o2.num)
o2.__class__ = A
o2.method()
print(o1.num, o2.num)
