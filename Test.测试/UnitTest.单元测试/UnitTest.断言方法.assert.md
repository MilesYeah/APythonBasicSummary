# 断言方法

在 UnitTest 中，TestCase 已经提供有封装好的断言方法进行断言校验。

断言： 用于校验实际结果与预期结果是否匹配。

在断言的内容上是有要求的，断言强调的是对于整个测试流程的结果进行断言。

常用的断言方式：
1. 验证页面html中是否包含想要的字段。  极弱
2. 定位需要验证的特定元素，是否包含想要的内容。  更强
3. 也可以验证某些元素的属性符合预期。
4. 验证页面查到的内容是否和数据库中查到的内容一致。  最强



* unittest.TestCase 类
* 6个核实方法
  * assertEqual(a, b)
  * assertNotEqual(a, b)
  * assertTrue(x)
  * assertFalse(x)
  * assertIn(item, list)
  * assertNotIn(item, list)


| method                                                              | explaination |
| ------------------------------------------------------------------- | ------------ |
| assertEqual(first, second, msg=None)                                |              |
| assertNotEqual(first, second, msg=None)                             |              |
| assertTrue(expr, msg=None)                                          |              |
| assertFalse(expr, msg=None)                                         |              |
| assertIs(first, second, msg=None)                                   |              |
| assertIsNot(first, second, msg=None)                                |              |
| assertIsNone(expr, msg=None)                                        |              |
| assertIsNotNone(expr, msg=None)                                     |              |
| assertIn(member, container, msg=None)                               |              |
| assertNotIn(member, container, msg=None)                            |              |
| assertIsInstance(obj, cls, msg=None)                                |              |
| assertNotIsInstance(obj, cls, msg=None)                             |              |
| assertRaises(exception, callable, *args, **kwds)                    |              |
| assertRaises(exception, *, msg=None)                                |              |
| assertRaisesRegex(exception, regex, callable, *args, **kwds)        |              |
| assertRaisesRegex(exception, regex, *, msg=None)                    |              |
| assertWarns(warning, callable, *args, **kwds)                       |              |
| assertWarns(warning, *, msg=None)                                   |              |
| assertWarnsRegex(warning, regex, callable, *args, **kwds)           |              |
| assertWarnsRegex(warning, regex, *, msg=None)                       |              |
| assertLogs(logger=None, level=None)                                 |              |
| assertAlmostEqual(first, second, places=7, msg=None, delta=None)    |              |
| assertNotAlmostEqual(first, second, places=7, msg=None, delta=None) |              |
| assertGreater(first, second, msg=None)                              |              |
| assertGreaterEqual(first, second, msg=None)                         |              |
| assertLess(first, second, msg=None)                                 |              |
| assertLessEqual(first, second, msg=None)                            |              |
| assertRegex(text, regex, msg=None)                                  |              |
| assertNotRegex(text, regex, msg=None)                               |              |
| assertCountEqual(first, second, msg=None)                           |              |
| addTypeEqualityFunc(typeobj, function)                              |              |
| assertMultiLineEqual(first, second, msg=None)                       |              |
| assertSequenceEqual(first, second, msg=None, seq_type=None)         |              |
| assertListEqual(first, second, msg=None)                            |              |
| assertTupleEqual(first, second, msg=None)                           |              |
| assertSetEqual(first, second, msg=None)                             |              |
| assertDictEqual(first, second, msg=None)                            |              |







| Method                                        | Checks that                                                    | New in |
| --------------------------------------------- | -------------------------------------------------------------- | ------ |
| assertRaises(exc, fun, *args, **kwds)         | fun(*args, **kwds) raises exc                                  |        |
| assertRaisesRegex(exc, r, fun, *args, **kwds) | fun(*args, **kwds) raises exc and the message matches regex r  | 3.1    |
| assertWarns(warn, fun, *args, **kwds)         | fun(*args, **kwds) raises warn                                 | 3.2    |
| assertWarnsRegex(warn, r, fun, *args, **kwds) | fun(*args, **kwds) raises warn and the message matches regex r | 3.2    |
| assertLogs(logger, level)                     | The with block logs on logger with minimum level               | 3.4    |





| Method                     | Checks that                                                                   | New in |
| -------------------------- | ----------------------------------------------------------------------------- | ------ |
| assertAlmostEqual(a, b)    | round(a-b, 7) == 0                                                            |        |
| assertNotAlmostEqual(a, b) | round(a-b, 7) != 0                                                            |        |
| assertGreater(a, b)        | a > b                                                                         | 3.1    |
| assertGreaterEqual(a, b)   | a >= b                                                                        | 3.1    |
| assertLess(a, b)           | a < b                                                                         | 3.1    |
| assertLessEqual(a, b)      | a <= b                                                                        | 3.1    |
| assertRegex(s, r)          | r.search(s)                                                                   | 3.1    |
| assertNotRegex(s, r)       | not r.search(s)                                                               | 3.2    |
| assertCountEqual(a, b)     | a and b have the same elements in the same number, regardless of their order. | 3.2    |


