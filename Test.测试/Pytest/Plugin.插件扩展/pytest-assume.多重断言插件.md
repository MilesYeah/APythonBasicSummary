# pytest-assume 多重断言插件



一个方法中写了多条断言，通常第一条过不去，下面的就不执行了，我们希望第一条报错之后，后面的也能够正常运行

```
pip install pytest-assume 
```


## 实例

使用pytest.assume()，代码如下：
```py
import pytest

class Test_A():

    def test_case01(self):
        print(f"测试用例1")
        pytest.assume(1 < 2)
        pytest.assume('a' == 'a')
        pytest.assume(1 < 1)
        pytest.assume(1 == 1)
        pytest.assume(1 > 2)

```

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tPytestAssume.py
Testing started at 18:31 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tPytestAssume.py --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest\tFixture

============================= test session starts =============================
collecting ... collected 1 item

tPytestAssume.py::Test_A::test_case01 FAILED                             [100%]测试用例1

tPytestAssume.py:4 (Test_A.test_case01)
tp = <class 'pytest_assume.plugin.FailedAssumption'>, value = None, tb = None

    def reraise(tp, value, tb=None):
        try:
            if value is None:
                value = tp()
            if value.__traceback__ is not tb:
>               raise value.with_traceback(tb)
E               pytest_assume.plugin.FailedAssumption: 
E               2 Failed Assumptions:
E               
E               tPytestAssume.py:9: AssumptionFailure
E               >>	pytest.assume(1 < 1)
E               AssertionError: assert False
E               
E               tPytestAssume.py:11: AssumptionFailure
E               >>	pytest.assume(1 > 2)
E               AssertionError: assert False

C:\Users\Envs\trials\lib\site-packages\six.py:718: FailedAssumption




============================== 1 failed in 0.30s ==============================

Process finished with exit code 1

```














## ref
* [版权声明：本文为CSDN博主「杜雨成」的原创文章，遵循CC](https://blog.csdn.net/qq_41780297/article/details/114214694)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()

