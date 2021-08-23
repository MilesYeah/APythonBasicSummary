# @unpack


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

