# parameterized.unittest参数化



```py
import unittest
from nose_parameterized import parameterized, param

class TestAdd(unittest.TestCase):

    @parameterized.expand([
        param("11", 11),
        param("10", 16, base=16),
    ])
    def test_int(self, str_val, expected, base=10):
        self.assertEqual(int(str_val, base), expected)


if __name__ == '__main__':
    unittest.main()
```

test_int会运行两组参数：
第一组：(str_val=”11”, expected=11, base=10)
第二组：(str_val=”10”, expected=16, base=16)
即在@parameterized.expand的param中可以默认指定参数的值，且此值不会随方法的变量改变








## ref
* [unittest参数化parameterized](https://blog.csdn.net/u010895119/article/details/74452745)
* []()
* []()
* []()
* []()
* []()
* []()

