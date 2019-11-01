
from collections.abc import Iterable
from collections.abc import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.curr_count = 0
    def add(self, name):
        self.names.append(name)
    def __iter__(self):
        """如果想要一个对象称之为可迭代对象，即可以用for，那么必须实现__iter__方法。
        而且该方法必须返回一个对象的引用(而且要实现__iter__和__next__)"""
        return self
    def __next__(self):
        if self.curr_count < len(self.names):
            ret = self.names[self.curr_count]
            self.curr_count += 1
            return ret
        else:
            self.curr_count = 0
            raise StopIteration

obj_mate = Classmate()
obj_mate.add("wanger")
obj_mate.add("zhangsan")
obj_mate.add("lisi")

# obj_iter = ClassIterator(obj_mate)

print("whether object obj_mate is iterable: ", isinstance(obj_mate, Iterable))
# print("whether object obj_iter is iterator: ", isinstance(obj_iter, Iterator))
# print(next(obj_iter))
for i in obj_mate:
    print(i)
