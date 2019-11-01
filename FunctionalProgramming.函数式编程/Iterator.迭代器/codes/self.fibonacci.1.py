"""
specify the max value, return the values from Fibonacci which are smaller than the max value.
"""

class Fibonacci(object):

    def __init__(self, max_num):
        self.max_num = max_num
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a < self.max_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            return ret
        else:
            raise StopIteration

print(Fibonacci(100))
for i in Fibonacci(100):
    print(i)
