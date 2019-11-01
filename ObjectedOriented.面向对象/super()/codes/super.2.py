
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
        super(Son2, self).__init__()
        print("Leaving GrandSon")

print(GrandSon.__mro__)
o = GrandSon()


"""result
(<class '__main__.GrandSon'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
Enter GrandSon
Enter Parent
Leaving Parent
Leaving GrandSon
"""
