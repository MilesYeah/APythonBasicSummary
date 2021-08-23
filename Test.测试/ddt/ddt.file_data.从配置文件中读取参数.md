# @file_data

file_data 读取配置文件的时候，其默认编码为 utf8 ，所以有时候在使用中文配置文件的时候，会出现读取配置文件出错的问题。
如果出现这个问题，那么我们可以来到 file_data 定义的源码部分，将 with open 的编码改掉，例如 gbk 编码。


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


