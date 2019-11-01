
class A(object):
    def __init__(self):
        print("Enter A")
        super(A, self).__init__()
        print("Leaving A")

class B(object):
    def __init__(self):
        print("Enter B")
        super(B, self).__init__()
        print("Leaving B")


class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leaving C")

# class D(object):
class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leaving D")

class E(B, C):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leaving E")

class F(E, D):
    def __init__(self):
        print("Enter F")
        super(F, self).__init__()
        print("Leaving F")


f = F()
