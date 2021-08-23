# Pytest.mark.用例标签

## 给某个方法加上标签 webtest
```py
import pytest

class Test_错误密码2:

    @pytest.mark.webtest
    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```

然后，可以这样运行指定标签的用例
```py
$ pytest -v -m webtest
$ pytest -v -m "not webtest"
$ pytest -v test_server.py::TestClass::test_method
$ pytest -v test_server.py::TestClass
$ pytest -v test_server.py::TestClass test_server.py::test_send_http
$ pytest -v -k http  # running with the above defined example module
$ pytest -k "not send_http" -v
$ pytest -k "http or quick" -v

```

## 给整个类加上标签
```py
@pytest.mark.webtest
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```


## 当然标签也支持中文
```py
@pytest.mark.网页测试
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```

然后，运行命令行指定标签
```py
pytest cases -m 网页测试 -s
```


## 同时添加多个标签
```py
@pytest.mark.网页测试
@pytest.mark.登录测试
class Test_错误密码2:

    def test_C001021(self):
        print('\n用例C001021')
        assert 1 == 1
```



## 给模块级别添加标签

### 定义一个全局变量 
要在模块级别应用标记，请使用pytestmark全局变量：

pytestmark 为 整个模块文件 设定标签
```py
import pytest
pytestmark = pytest.mark.webtest
```


### 定义一个标签列表
```py
import pytest
pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]

```

## marker 结合参数化
```py
import pytest


@pytest.mark.foo
@pytest.mark.parametrize(
    ("n", "expected"), [(1, 2), pytest.param(1, 3, marks=pytest.mark.bar), (2, 3)]
)
def test_increment(n, expected):
    assert n + 1 == expected
```


## 注册 markers

```py
# content of pytest.ini
[pytest]
addopts = -sv --html=../report/report_from_ini.html
testpaths = ./test_case_ini
python_files = test*.py
python_classes = Test*
python_functions = test*
markers = 
    smoke: 冒烟
    userManage: 用户管理
    productManage: 产品管理

```
通过在自己的行中定义每个自定义标记，可以注册多个自定义标记，如上面的示例所示。

您可以查询您的测试套件中存在哪些 marker -该列表包括我们刚刚定义的webtest和slow标记：


```ps1
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
PS F:\Development\Trials\tPytest> pytest --markers
@pytest.mark.smoke: 鍐掔儫

@pytest.mark.userManage: 鐢ㄦ埛绠＄悊

@pytest.mark.productManage: 浜у搧绠＄悊

@pytest.mark.forked: Always fork for this test.

@pytest.mark.nondestructive: mark the test as nondestructive. Tests are assumed to be destructive unless this marker is present. This reduces the risk of running destructive tests accidentally.

@pytest.mark.firefox_arguments(args): arguments to be passed to Firefox. This marker will be ignored for other browsers. For example: firefox_arguments('-foreground')

@pytest.mark.firefox_preferences(dict): preferences to be passed to Firefox. This marker will be ignored for other browsers. For example: firefox_preferences({'browser.startup.homepage': 'https://pytest.org/'})

@pytest.mark.flaky(reruns=1, reruns_delay=0): mark test to re-run up to 'reruns' times. Add a delay of 'reruns_delay' seconds between re-runs.

@pytest.mark.run: specify ordering information for when tests should run in relation to one another. Provided by pytest-ordering. See also: http://pytest-ordering.readthedocs.org/

@pytest.mark.allure_label: allure label marker

@pytest.mark.allure_link: allure link marker

@pytest.mark.allure_description: allure description

@pytest.mark.allure_description_html: allure description html

@pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/warnings.html#pytest-mark-filterwarnings

@pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of currently testing this") skips the test.

@pytest.mark.skipif(condition, ..., *, reason=...): skip the given test function if any of the conditions evaluate to True. Example: skipif(sys.platform == 'win32') skips the test if we are on the win32 platform. See https://docs.pytes
t.org/en/stable/reference.html#pytest-mark-skipif

@pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=xfail_strict): mark the test function as an expected failure if any of the conditions evaluate to True. Optionally specify a reason for better reporting an
d run=False if you don't even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if the test fails in other ways, it will be reported as a true failure. See https://docs.pyte
st.org/en/stable/reference.html#pytest-mark-xfail

@pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of valu
es if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.pytest.org/en/stable/parametrize.html for mo
re info and examples.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/stable/fixture.html#usefixtures

@pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as early as possible.

@pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as late as possible.

@pytest.mark.capabilities(kwargs): add or change existing capabilities. specify capabilities as keyword arguments, for example capabilities(foo=bar)

PS F:\Development\Trials\tPytest>
```



## 为pytest标记平台特定测试

假设您有一个测试套件，它为特定的平台（即pytest.mark.darwin、pytest.mark.win32等）标记测试，并且您也有在所有平台上运行的测试，并且没有特定的标记。

如果您现在想只运行特定平台的测试，可以使用以下插件：
```py
# content of conftest.py
#
import sys
import pytest

ALL = set("darwin linux win32".split())


def pytest_runtest_setup(item):
    supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
    plat = sys.platform
    if supported_platforms and plat not in supported_platforms:
        pytest.skip("cannot run on platform {}".format(plat))
```

如果为不同的平台指定了测试，则将跳过这些测试。让我们做一个小测试文件来展示它的样子：
```py
# content of test_plat.py

import pytest


@pytest.mark.darwin
def test_if_apple_is_evil():
    pass


@pytest.mark.linux
def test_if_linux_works():
    pass


@pytest.mark.win32
def test_if_win32_crashes():
    pass


def test_runs_everywhere():
    pass
```
然后您将看到两个被跳过的测试和两个按预期执行的测试：
```py
$ pytest -rs # this option reports skip reasons
$ pytest -m linux
```
然后未标记的测试则不会运行。 因此，这是一种将运行限制到特定测试的方法。



## 基于测试名称自动添加标记

如果您有一个测试套件，其中的测试函数名表示某种类型的测试，那么您可以实现一个钩子来自动定义标记，这样您就可以对它使用 `-m` 选项。
```py
# content of test_module.py
def test_interface_simple():
    assert 0


def test_interface_complex():
    assert 0


def test_event_simple():
    assert 0


def test_something_else():
    assert 0
```


我们希望动态定义两个标记，并可以在conftest.py插件中执行：
```py
# content of conftest.py
import pytest

def pytest_collection_modifyitems(items):
    for item in items:
        if "interface" in item.nodeid:
            item.add_marker(pytest.mark.interface)
        elif "event" in item.nodeid:
            item.add_marker(pytest.mark.event)
```

```sh
$ pytest -m interface --tb=short                    # 我们现在可以使用-m选项选择一个集合
$ pytest -m "interface or event" --tb=short         # 选择“事件”和“接口”测试：
```











## ref
* [参考官方文档](https://docs.pytest.org/en/latest/example/markers.html)
* [pytest 框架](http://www.byhy.net/tut/auto/pytest/01/#%E6%8C%91%E9%80%89%E7%94%A8%E4%BE%8B%E6%89%A7%E8%A1%8C)
* []()
* []()
* []()
* []()
* []()
* []()
