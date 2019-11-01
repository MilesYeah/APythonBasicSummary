
class Parent(object): 
    def __init__(self):
        print("Enter Parent")
        super().__init__()
        print("Leaving Parent")

class Son1(Parent): 
    def __init__(self):
        print("Enter Son1")
        super().__init__()
        print("Leaving Son1")

class Son2(Parent): 
    def __init__(self):
        print("Enter Son2")
        super().__init__()
        print("Leaving Son2")

class GrandSon(Son1, Son2): 
    def __init__(self):
        print("Enter GrandSon")
        super().__init__()
        print("Leaving GrandSon")

print(GrandSon.__mro__)
o = GrandSon()
