# @data


```py
import os
import time
import unittest
# import HTML
from selenium import webdriver
from ddt import ddt, data, unpack, file_data
import yaml


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


if __name__ == "__main__":
    unittest.main()
```

