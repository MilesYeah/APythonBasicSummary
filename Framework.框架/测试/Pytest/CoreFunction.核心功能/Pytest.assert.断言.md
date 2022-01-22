# Pytest.assert.断言

<!-- ![](../UnitTest.单元测试/UnitTest.断言方法.assert.md) -->

| 语句                | 解释            |
| ------------------- | --------------- |
| `assert xx`         | 判断 xx 为真    |
| `assert not xx`     | 判断 xx 不为真  |
| `assert a > b`      | 判断 a 大于 b   |
| `assert a < b`      | 判断 a 小于 b   |
| `assert a != b`     | 判断 a 不等于 b |
| `assert a in b`     | 判断 b 包含 a   |
| `assert a not in b` | 判断 b 不包含 a |
|                     |                 |
|                     |                 |

与unittest不同，pytest使用的是python自带的assert关键字来进行断言

assert关键字后面可以接一个表达式，只要表达式的最终结果为True，那么断言通过，用例执行成功，否则用例执行失败

测试的主要工作目标就是验证实际结果与预期结果是否一致；在接口自动化测试中，通过断言来实现这一目标。Pytest中断言是通过assert语句实现的（pytest对Python原生的assert语句进行了优化），确定实际情况是否与预期一致。


## pytest断言assert的用法

在自动化测试用例中，最常用的断言是相等断言，就是断言预期结果和实际结果是一致的。pytest通过 “assert 实际结果 == 预期结果” 实现。通常我们断言的预期结果和实际结果的数据类型包括字符串、元组、字典、列表和对象。


## 断言字符串
```py
# content of test_assertions.py
class TestAssertions(object):
    def test_string(self):
        assert "spam" == "eggs"
```

说明：Expected 为期望结果（即 == 右侧的预期结果），Actual 为实际结果（即 == 左侧的实际结果），> 后面为出错的代码行，E 后面为错误信息。



## 断言函数返回值
```py
class TestAssertions(object):
    def test_function(self):
        def f():
            return [1, 2, 3]
        
        assert f() == [1, 2, 4]
```





## 断言集合类型

断言字典、列表、元组和集合等类型在测试中也是很常见的。比如下面这段测试用例代码：
```py
class TestCollections(object):
    def test_dict(self):
        assert {"a": 0, "b": 1, "c": 0} == {"a": 0, "b": 2, "d": 0}

    def test_dict2(self):
        assert {"a": 0, "b": {"c": 0}} == {"a": 0, "b": {"c": 2}}

    def test_list(self):
        assert [0, 1, 2] == [0, 1, 3]
        
    def test_list2(self):
        assert [0, 1, 2] == [0, 1, [1, 2]]

    def test_tuple(self):
        assert (0, 1, 2) ==(0, 1, 3)

    def test_set(self):
        assert {0, 10, 11, 12} == {0, 20, 21}
```





## Pytest断言Excepiton

除了支持对代码正常运行的结果断言之外，Pytest也能够对 Exception 和 Warnning 进行断言，来断定某种条件下，一定会出现某种异常或者警告。在功能测试和集成测试中，这两类断言用的不多，这里简单介绍一下。

对于异常的断言，Pytest的语法是：with pytest.raises(异常类型)，可以看下面的这个例子：
```py
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

这个测试用例断言运算表达式1除以0会产生ZeroDivisionError异常。除了对异常类型进行断言，还可以对异常信息进行断言，比如：
```py
# content of test_assertions.py
class TestAssertions(object):
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as excinfo:
            1 / 0
        assert 'division by zero' in str(excinfo.value)
```

这个测试用例，就断言了excinfo.value的内容中包含division by zero这个字符串，这在需要断言具体的异常信息时非常有用。


### match
```py
def test_01():
    with pytest.raises(ZeroDivisionError, match="zero") as e:
        1 / 0


def test_02():
    with pytest.raises(ZeroDivisionError, match=".*zero.*") as e:
        1 / 0
```

```
PS F:\Mirror\SourceCode\trials\tPytest> pytest.exe  -v  .\pAssert\test_match.py
==================================== test session starts ====================================
platform win32 -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- C:\Users\robert.ye\E
nvs\trials\Scripts\python.exe
cachedir: .pytest_cache
rootdir: F:\Mirror\SourceCode\trials\tPytest
plugins: allure-pytest-2.9.45, anyio-3.3.4, rerunfailures-10.2
collected 3 items                                                                            

pAssert/test_match.py::test_01 PASSED                                                  [ 33%]
pAssert/test_match.py::test_02 PASSED                                                  [ 66%]
pAssert/test_match.py::TestAssertions::test_zero_division PASSED                       [100%]

===================================== 3 passed in 0.03s =====================================
PS F:\Mirror\SourceCode\trials\tPytest>
```








## 优化断言

我们可以在异常的时候，输出一些提示信息。这样报错后。可以方便我们来查看原因。

拿最开始的例子来说，在assert后面加上说明（在断言等式后面加上 , 然在后写上说明信息）：
```py
# content of test_assertions.py
class TestAssertions(object):
    def test_string(self):
        assert "spam" == "eggs","校验字符串'spam'是否等于'eggs'"
```

这样当断言失败的时候，会给出自己写的失败原因了 E  AssertionError: 校验字符串'spam'是否等于'eggs'









## 断言装饰器

```py
import pytest

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_01():
    1 / 0
```

```
PS F:\Mirror\SourceCode\trials\tPytest> pytest.exe .\pAssert\decoratorAssert.py
==================================== test session starts ====================================
platform win32 -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: F:\Mirror\SourceCode\trials\tPytest
plugins: allure-pytest-2.9.45, anyio-3.3.4, rerunfailures-10.2
collected 1 item                                                                             

pAssert\decoratorAssert.py x                                                           [100%]

==================================== 1 xfailed in 0.44s =====================================
PS F:\Mirror\SourceCode\trials\tPytest>
```








## ref

* [Pytest的官方文档 Demo of Python failure reports with pytest](https://docs.pytest.org/en/latest/example/reportingdemo.html)
* [Warnning的断言可以参考Pytest的官方文档](https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions)
* [Pytest系列（2） - assert断言详细使用 - 小菠萝测试笔记 -  ](https://www.cnblogs.com/poloyy/p/12641778.html)
* []()
* []()
* []()
* []()
* []()
* []()

