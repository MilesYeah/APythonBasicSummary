
def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    # test2(a, b, args, kwargs)     # 相当于test2(1, 2, (3, 4, 5, 6), {'name': 'Robert', 'age': 18})
    # test2(a, b, *args, kwargs)    # 相当于test2(1, 2, 3, 4, 5, 6, {'name': 'Robert', 'age': 18})
    test2(a, b, *args, **kwargs)    # 相当于test2(1, 2, 3, 4, 5, 6, 'name': 'Robert', 'age': 18)


def test2(a, b, *args, **kwargs):
    print("-" * 10)
    print(a)
    print(b)
    print(args)
    print(kwargs)


test1(1, 2, 3, 4, 5, 6, name='Robert', age='18')

