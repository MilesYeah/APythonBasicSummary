# UnitTest.skip

在 case 中，对于不需要运行的用例或者特定条件下不执行的用例，可以应用 skip() 来实现有条件执行，或者绝对性跳过，用于对指定用例进行不执行操作。

| method                                  | explaination                                 |
| --------------------------------------- | -------------------------------------------- |
| @unittest.skip(reason)                  | 跳过测试用例，reason  为测试被跳过的原因     |
| @unittest.skipIf(condition, reason)     | 当 condition 为真时，跳过测试用例。          |
| @unittest.skipUnless(condition, reason) | 跳过测试用例，除非 condition 为真            |
| @unittest.expectedFailure               | 把测试用例标记为预计失败；                   |
|                                         | 如果测试不通过，会被认为测试成功；           |
|                                         | 如果测试通过了，则被认为是测试失败           |
| exception unittest.SkipTest(reason)     | 在方法体内满足某些条件下才跳过执行该测试用例 |
|                                         |                                              |
|                                         |                                              |
|                                         |                                              |


跳过执行测试用例注意点
* 被跳过的测试的  setUp() 和  tearDown()  不会被运行
* 只输入 unittest.skip ，也可以正常跳过，不必写reason
* 若输入 unittest.skip() ，括号内必须写reason，不得为空
* 可以针对单元测试类级别设置跳过执行（在class声明上面直接加装饰器即可），该单元测试类所有测试用例不会被执行
* 被跳过的类的 setUpClass() 和 tearDownClass() 不会被运行
* 当方法体内调用了 self.skipTest(reason) 方法，该测试用例还是会调用 setUp() 和 tearDown() 



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

