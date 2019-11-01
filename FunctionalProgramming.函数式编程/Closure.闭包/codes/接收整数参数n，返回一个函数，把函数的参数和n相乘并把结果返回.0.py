import functools
def close(base):
    def wrap(num):
        return base * num
    return wrap

f = close(10)
print(f(20))

f2 = close(2)
print(f2(8))
