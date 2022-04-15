# @unpack

1. @unpack ：当传递的是复杂的数据结构时使用。比如使用元组或者列表，添加 @unpack 之后， ddt 会自动把元组或者列表对应到多个参数上。字典也可以这样处理
2. 当没有加unpack时，test_case方法的参数只能填一个；如元组的例子
3. 当你加了unpack时，传递的数据量需要一致；如列表例子中，每个列表我都固定传了三个数据，当你多传或少传时会报错，而test_case方法的参数也要写三个，需要匹配上
4. 当传的数据是字典类型时，要注意每个字典的key都要一致，test_case的参数的命名也要一致；如字典的例子，两个字典的key都是value1和value2，而方法的参数也是
5. 当传的数据是通过变量的方式，如元组2、列表2，变量前需要加上*

## 实例2

```py
from ddt import *


# 在测试类前必须首先声明使用 ddt
@ddt
class imoocTest(unittest.TestCase):
    tuples = ((1, 2, 3), (1, 2, 3))
    lists = [[1, 2, 3], [1, 2, 3]]

    # 元组
    @data((1, 2, 3), (1, 2, 3))
    def test_tuple(self, n):
        print("test_tuple", n)

    # 列表
    @data([1, 2, 3], [1, 2, 3])
    @unpack
    def test_list(self, n1, n2, n3):
        print("test_list", n1, n2, n3)

    # 元组2
    @data(*tuples)
    def test_tuples(self, n):
        print("test_tuples", n)

    # 列表2
    @data(*lists)
    @unpack
    def test_lists(self, n1, n2, n3):
        print("test_lists", n1, n2, n3)

    # 字典
    @data({'value1': 1, 'value2': 2}, {'value1': 1, 'value2': 2})
    @unpack
    def test_dict(self, value1, value2):
        print("test_dict", value1, value2)
```
结果
```
test_dict 1 2
test_dict 1 2
test_list 1 2 3
test_list 1 2 3
test_lists 1 2 3
test_lists 1 2 3
test_tuple (1, 2, 3)
test_tuple (1, 2, 3)
test_tuples (1, 2, 3)
test_tuples (1, 2, 3)
```



## 实例1
```txt  paras.txt
abc,def
haha,hehe
heihei,happy
```

```py
import os
import time
import unittest
# import HTML
from selenium import webdriver
from ddt import ddt, data, unpack, file_data
import yaml


def get_paras_from_file():
    ret = []
    with open("paras.txt", 'r') as f:
        for line in f.readlines():
            paras = line.strip().split(',')
            ret.append(paras)
    return ret


@ddt
class tUnittestDdt(unittest.TestCase):

    @data(("what", 'a'), ('nice', 'day'))
    @unpack
    def test_ddt_2paras(self, txt, p2):
        print(f"Test data: {txt} {p2}")

    @data(*get_paras_from_file())
    @unpack
    def test_ddt_paras_from_file(self, txt, p2):
        print(f"Test data: {txt} {p2}")


if __name__ == "__main__":
    unittest.main()
```

