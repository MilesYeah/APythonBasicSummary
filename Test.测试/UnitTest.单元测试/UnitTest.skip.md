# UnitTest.skip

在 case 中，对于不需要运行的用例或者特定条件下不执行的用例，可以应用 skip() 来实现有条件执行，或者绝对性跳过，用于对指定用例进行不执行操作。

| method                                  | explaination                 |
| --------------------------------------- | ---------------------------- |
| @unittest.skip(reason)                  | 无条件逃过当前用例           |
| @unittest.skipIf(condition, reason)     | 如果条件满足则跳过           |
| @unittest.skipUnless(condition, reason) | 除非条件满足，就执行         |
| @unittest.expectedFailure               | 即使失败，也不计算为失败案例 |
| exception unittest.SkipTest(reason)     |                              |



Classes can be skipped just like methods:
```py
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```


自定义 skip 装饰器
```py
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```





```py
import unittest


class tUnittestSkip(unittest.TestCase):

    @unittest.skip('就是不想执行')
    def test_skip1(self):
        print("test_skip1")

    @unittest.skipIf(1 < 2, '1 < 2 if 就跳过执行')
    def test_skip2(self):
        print("test_skip2")

    @unittest.skipUnless(1 > 2, '1 > 2 unless 就跳过执行')
    def test_skip3(self):
        print("test_skip3")

    @unittest.expectedFailure
    def test_skip4(self):
        self.assertEqual(2, 3, "notEqual")
        print("test_skip4")

    # def test_skip5(self):
    #     self.assertEqual(2, 3, "notEqual")
    #     print("test_skip5")


if __name__ == "__main__":
    unittest.main()
```

