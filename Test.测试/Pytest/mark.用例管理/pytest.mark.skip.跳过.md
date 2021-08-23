# pytest.mark.skip
[URL pytest.mark.skip](https://docs.pytest.org/en/stable/reference.html#pytest.mark.skip)


## @pytest.mark.skip
### 装饰器调用 @pytest.mark.skip(reason="xxx"）
```py
@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    ...
```


### 直接调用 pytest.skip(reason)
或者，也可以通过调用 pytest.skip（reason） 函数在测试执行或设置期间强制跳过：
```py
def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
```

在导入期间无法评估跳过条件时，命令式方法非常有用。



### allow_module_level=True
也可以在模块级使用 pytest.skip（reason, allow_module_level=True）跳过整个模块：
```py
import sys
import pytest

if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)
```



## @pytest.mark.skipif

### 条件跳过 pytest.mark.skipif
[URL pytest.mark.skipif](https://docs.pytest.org/en/stable/reference.html#pytest.mark.skipif)


```py
import sys


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_function():
    ...
```

如果在收集期间条件的计算结果为True，则将跳过测试函数，并在使用`-rs`时在摘要中显示指定的原因。

可以在模块之间共享skipif标记。考虑这个测试模块：
```py
# content of test_mymodule.py
import mymodule

minversion = pytest.mark.skipif(
    mymodule.__versioninfo__ < (1, 1), reason="at least mymodule-1.1 required"
)


@minversion
def test_function():
    ...
```

You can import the marker and reuse it in another test module:
```py
# test_myothermodule.py
from test_mymodule import minversion


@minversion
def test_anotherfunction():
    ...
```



### 跳过类(标记装饰一个类)

可以在类上使用skipif标记（与任何其他标记一样）：

```py
@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function(self):
        "will not be setup or run under 'win32' platform"
```




## pytest.importorskip
### 跳过缺少的导入依赖项 pytest.importorskip("some_lib")

通过在模块级、测试或测试设置函数中使用pytest.importorskip，可以跳过缺少导入的测试。

```py
docutils = pytest.importorskip("docutils")
```

如果不能在这里导入docutils，这将导致跳过测试结果。也可以根据库的版本号跳过：

```py
docutils = pytest.importorskip("docutils", minversion="0.3")
```

The version will be read from the specified module’s __version__ attribute.




## 总结
Here’s a quick guide on how to skip tests in a module in different situations:

无条件跳过模块中的所有测试：
```py
pytestmark = pytest.mark.skip("all tests still WIP")
```

根据某些条件跳过模块中的所有测试：
```py
pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
```

如果缺少某些导入，请跳过模块中的所有测试：
```py
pexpect = pytest.importorskip("pexpect")
```




## 实例

### 1

```py
import pytest


class TestOrder():
    age = 10

    @pytest.mark.run(order=3)
    def test_o1(self):
        print("test O1")

    @pytest.mark.run(order=1)
    @pytest.mark.skipif(age < 18, reason="Skip if age is less than 18")
    def test_o2(self):
        print("test O4")

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(age > 18, reason="Skip if age is greater than 18")
    def test_o3(self):
        print("test O3")

    @pytest.mark.run(order=4)
    @pytest.mark.skip("No need to run #4")
    def test_o4(self):
        print("test O4")


if __name__ == '__main__':
    pytest.main()

```

```sh
C:\Users\robert.ye\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Development/Trials/tPytest1/test_APIs/test_mark_skip.py
Testing started at 19:43 ...
Launching pytest with arguments F:/Development/Trials/tPytest1/test_APIs/test_mark_skip.py --no-header --no-summary -q in F:\Development\Trials\tPytest1\test_APIs

============================= test session starts =============================
collecting ... collected 4 items

test_mark_skip.py::TestOrder::test_o2 
test_mark_skip.py::TestOrder::test_o3 
test_mark_skip.py::TestOrder::test_o1 
test_mark_skip.py::TestOrder::test_o4 

======================== 2 passed, 2 skipped in 0.13s =========================

Process finished with exit code 0
SKIPPED                            [ 25%]
Skipped: Skip if age is less than 18
PASSED                             [ 50%]test O3
PASSED                             [ 75%]test O1
SKIPPED                            [100%]
Skipped: No need to run #4

```

### 2

```py

```

```sh

```

