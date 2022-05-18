# @file_data

file_data 读取配置文件的时候，其默认编码为 utf8 ，所以有时候在使用中文配置文件的时候，会出现读取配置文件出错的问题。

如果出现这个问题，那么我们可以来到 file_data 定义的源码部分，将 with open 的编码改掉，例如 gbk 编码。


## 传递 JSON 文件
testddt.json
```json
{
  "first": [
    {
      "isRememberMe": "True",
      "password": "111111",
      "username": "root"
    },
    "200"
  ],
  "second": [
    "{'isRememberMe': True, 'password': '1111111', 'username': 'root'}",
    "406"
  ],
  "third": [
    1,
    2
  ],
  "four": "123123"
}
```
```py
from ddt import *


# 在测试类前必须首先声明使用 ddt
@ddt
class imoocTest(unittest.TestCase):

    @file_data('F:/test/config/testddt.json')
    def test_json(self, data):
        print(data)
```
运行结果
```
[{'isRememberMe': 'True', 'password': '111111', 'username': 'root'}, '200']
["{'isRememberMe': True, 'password': '1111111', 'username': 'root'}", '406']
[1, 2]
123123
```





## 传递 YAML 文件

```txt  paras.txt
abc,def
haha,hehe
heihei,happy
```

```yml  file_data1.yml
name: "www"
info: "info"
```
```yml  file_data2.yml
- name: "Robert"
  text: "handsome"
- name: "Sophia"
  text: "beautiful"
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

    @data(*get_paras_from_file())
    @unpack
    def test_ddt_paras_from_file(self, txt, p2):
        print(f"Test data: {txt} {p2}")

    @file_data("file_data1.yml")
    def test_ddt_file_data(self, p1):
        print(p1)

    @file_data("file_data2.yml")
    def test_ddt_file_data(self, **kwargs):
        print("---------------------------")
        print(kwargs.get("name"))
        print(kwargs.get("text"))


if __name__ == "__main__":
    unittest.main()
```


