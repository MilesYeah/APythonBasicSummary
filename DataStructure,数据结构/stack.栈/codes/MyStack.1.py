
class MyStack(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.data)
print(s.pop())
print(s.pop())
print(s)
print(s.data)
