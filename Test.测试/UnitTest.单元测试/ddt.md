# ddt



```txt  paras.txt
abc,def
haha,hehe
heihei,happy
```
```yml  file_data.yml
name: "www"
info: "info"
```
```yml  1.yml
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

    @data("what", 'a', 'nice', 'day')
    def test_data(self, txt):
        print(f"Test data: {txt}")

    @data(("what", 'a'), ('nice', 'day'))
    @unpack
    def test_ddt_2paras(self, txt, p2):
        print(f"Test data: {txt} {p2}")

    @data(*get_paras_from_file())
    @unpack
    def test_ddt_paras_from_file(self, txt, p2):
        print(f"Test data: {txt} {p2}")

    @file_data("file_data.yml")
    def test_ddt_file_data(self, p1):
        print(p1)

    @file_data("1.yml")
    def test_ddt_file_data(self, **kwargs):
        print("---------------------------")
        print(kwargs.get("name"))
        print(kwargs.get("text"))


if __name__ == "__main__":
    unittest.main()
```
