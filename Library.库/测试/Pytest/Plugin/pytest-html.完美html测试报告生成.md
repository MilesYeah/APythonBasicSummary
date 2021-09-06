# pytest-html

生成简单的 html 报告，需要安装一个库 `pytest-html`. 直接使用 pip 就可以安装 `pip install pytest-html`

* `--html=report_filename.html` 命令行中添加该参数即可生成名为 `report_filename.html` 的测试报告，测试报告分为两部分，
  * assets 目录包含样式文件 如 css
  * report_filename.html 即测试报告
* `--self-contained-html` 该参数会将样式文件直接集成到 html 报告中。



## 实例 1
```py
# encoding: utf-8

"""
@author: 
Date: 4/27/2021 10:58 AM
docs: 
"""
import time
import pytest


class TestRerun(object):

    def test_01(self):
        n = 2
        print(f"Sleep {n}")
        assert n == 3

    def test_02(self):
        n = 3
        print(f"Sleep {n}")
        assert n == 2

    def test_03(self):
        n = 2
        print(f"Sleep {n}")

    def test_04(self):
        n = 4
        print(f"Sleep {n}")

    def test_05(self):
        n = 2
        print(f"Sleep {n}")


if __name__ == "__main__":
    print(time.time())
    pytest.main(['-v', '-s', './rerun.py', '--reruns=3', '-–html=./report.html'])
    print(time.time())
```



```sh
PS F:\Development\Trials\tPytest\test_case> pytest.exe .\test_rerun.py -v -s --reruns=3 --html=report.html
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\users\\envs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.17134-SP0', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.40', 'base-url': '1.4.2', 'forked': '1.3.0', 'html': '3.1.1',
 'metadata': '1.11.0', 'ordering': '0.6', 'rerunfailures': '9.1.1', 'selenium': '2.0.1', 'variables': '1.9.0', 'xdist': '2.2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2', 'Base URL': '', 'Driver': None, 'Capabilities': {}}
sensitiveurl: .*
rootdir: F:\Development\Trials\tPytest, configfile: pytest.ini
plugins: allure-pytest-2.8.40, base-url-1.4.2, forked-1.3.0, html-3.1.1, metadata-1.11.0, ordering-0.6, rerunfailures-9.1.1, selenium-2.0.1, variables-1.9.0, xdist-2.2.1
collected 5 items                                                                                                                                                                                                                         

test_rerun.py::TestRerun::test_01 Sleep 2
RERUN
test_rerun.py::TestRerun::test_01 Sleep 2
RERUN
test_rerun.py::TestRerun::test_01 Sleep 2
RERUN
test_rerun.py::TestRerun::test_01 Sleep 2
FAILED
test_rerun.py::TestRerun::test_02 Sleep 3
RERUN
test_rerun.py::TestRerun::test_02 Sleep 3
RERUN
test_rerun.py::TestRerun::test_02 Sleep 3
RERUN
test_rerun.py::TestRerun::test_02 Sleep 3
FAILED
test_rerun.py::TestRerun::test_03 Sleep 2
PASSED
test_rerun.py::TestRerun::test_04 Sleep 4
PASSED
test_rerun.py::TestRerun::test_05 Sleep 2
PASSED

================================================================================================================ FAILURES ================================================================================================================
___________________________________________________________________________________________________________ TestRerun.test_01 ____________________________________________________________________________________________________________

self = <tPytest.test_case.test_rerun.TestRerun object at 0x000001F7066EAAC0>

    def test_01(self):
        n = 2
        print(f"Sleep {n}")
>       assert n == 3
E       assert 2 == 3
E         +2
E         -3

test_rerun.py:18: AssertionError
___________________________________________________________________________________________________________ TestRerun.test_02 ____________________________________________________________________________________________________________

self = <tPytest.test_case.test_rerun.TestRerun object at 0x000001F70672DDF0>

    def test_02(self):
        n = 3
        print(f"Sleep {n}")
>       assert n == 2
E       assert 3 == 2
E         +3
E         -2

test_rerun.py:23: AssertionError
---------------------------------------------------------------------------- generated html file: file://F:\Development\Trials\tPytest\test_case\report.html -----------------------------------------------------------------------------
======================================================================================================== short test summary info =========================================================================================================
FAILED test_rerun.py::TestRerun::test_01 - assert 2 == 3
FAILED test_rerun.py::TestRerun::test_02 - assert 3 == 2
================================================================================================== 2 failed, 3 passed, 6 rerun in 0.26s ==================================================================================================
PS F:\Development\Trials\tPytest\test_case>
PS F:\Development\Trials\tPytest\test_case> ls


    Directory: F:\Development\Trials\tPytest\test_case


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        4/27/2021  11:01 AM                .pytest_cache
d-----        5/14/2021   8:52 PM                assets
d-----        4/27/2021   1:35 PM                __pycache__
-a----        4/16/2021  11:42 AM            273 case_03.py
-a----        4/16/2021  11:42 AM            784 deprecate_test_allure_decorations.py
-a----        4/16/2021  11:42 AM            918 deprecate_test_cookies.py
-a----        5/14/2021   8:52 PM          15604 report.html
-a----        4/16/2021   2:03 PM            423 test_case_class.py
-a----        4/16/2021   2:02 PM            507 test_case_function.py
-a----        4/27/2021  11:59 AM           1022 test_group.py
-a----        4/27/2021  11:10 AM            780 test_multithread.py
-a----        4/27/2021  11:27 AM            639 test_ordering.py
-a----        4/27/2021  11:24 AM            707 test_rerun.py
-a----        4/16/2021   2:30 PM           1123 test_selenium.py
-a----        4/16/2021  11:42 AM              0 __init__.py


PS F:\Development\Trials\tPytest\test_case>

```




## 实例 2

```sh
import pytest


def test_w1():
    print("test_w1")


def test_w2():
    print("test_w2")


def test_w3():
    print("test_w3")


if __name__ == "__main__":
    pytest.main(['-sv', 'rA', '-q', "test_html_report.py", '–-html=./report.html'])

    # pytest.exe -sv .\test_APIs\test_html_report.py -html="./report.html"
    # pytest.exe -sv .\test_APIs\test_html_report.py -html="./report.html" --self-contained-html

```


```sh

PS F:\Development\Trials\tPytest1> pytest.exe -sv .\test_APIs\test_html_report.py --html="./re
port.html"
==================================== test session starts ====================================
platform win32 -- Python 3.8.5, pytest-6.0.1, py-1.10.0, pluggy-0.13.1 -- c:\users\robert.ye\e
nvs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest':
'6.0.1', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.17', 'Faker':
'8.1.4', 'base-url': '1.4.2', 'forked': '1.3.0', 'html': '3.1.1', 'metadata': '1.11.0', 'order
ing': '0.6', 'rerunfailures': '9.1.1', 'selenium': '2.0.1', 'variables': '1.9.0', 'xdist': '2.
2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2', 'Base URL': '', 'Driver': None, 'Ca
pabilities': {}}
sensitiveurl: .*
rootdir: F:\Development\Trials\tPytest1
plugins: allure-pytest-2.8.17, Faker-8.1.4, base-url-1.4.2, forked-1.3.0, html-3.1.1, metadata
-1.11.0, ordering-0.6, rerunfailures-9.1.1, selenium-2.0.1, variables-1.9.0, xdist-2.2.1
collected 3 items                                                                            

test_APIs/test_html_report.py::test_w1 test_w1
PASSED
test_APIs/test_html_report.py::test_w2 test_w2
PASSED
test_APIs/test_html_report.py::test_w3 test_w3
PASSED

---------- generated html file: file://F:\Development\Trials\tPytest1\report.html -----------
===================================== 3 passed in 0.13s =====================================
PS F:\Development\Trials\tPytest1> ls


    目录: F:\Development\Trials\tPytest1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2021/8/18     13:42                .idea
d-----         2021/8/18     11:41                .pytest_cache
d-----         2021/8/18     13:43                assets
d-----         2021/8/18     13:44                test_APIs
d-----         2021/8/18     11:55                __pycache__
-a----         2021/8/18     11:57            155 apytest.ini
-a----         2021/8/18     13:44          12299 report.html


PS F:\Development\Trials\tPytest1>

```




### `--self-contained-html`

添加 `--self-contained-html` 参数之后，就会单独生成一个独立的 html ，css包含在了 html 文件中，
如果没有该参数，则会单独生成一个 assets 目录。

```sh

PS F:\Development\Trials\tPytest1> ls


    目录: F:\Development\Trials\tPytest1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2021/8/18     13:42                .idea
d-----         2021/8/18     11:41                .pytest_cache
d-----         2021/8/18     13:44                test_APIs
d-----         2021/8/18     11:55                __pycache__
-a----         2021/8/18     11:57            155 apytest.ini

PS F:\Development\Trials\tPytest1> pytest.exe -sv .\test_APIs\test_html_report.py --html="./re
port.html" --self-contained-html
==================================== test session starts ====================================
platform win32 -- Python 3.8.5, pytest-6.0.1, py-1.10.0, pluggy-0.13.1 -- c:\users\robert.ye\e
nvs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest':
'6.0.1', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.17', 'Faker':
'8.1.4', 'base-url': '1.4.2', 'forked': '1.3.0', 'html': '3.1.1', 'metadata': '1.11.0', 'order
ing': '0.6', 'rerunfailures': '9.1.1', 'selenium': '2.0.1', 'variables': '1.9.0', 'xdist': '2.
2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2', 'Base URL': '', 'Driver': None, 'Ca
pabilities': {}}
sensitiveurl: .*
rootdir: F:\Development\Trials\tPytest1
plugins: allure-pytest-2.8.17, Faker-8.1.4, base-url-1.4.2, forked-1.3.0, html-3.1.1, metadata
-1.11.0, ordering-0.6, rerunfailures-9.1.1, selenium-2.0.1, variables-1.9.0, xdist-2.2.1
collected 3 items                                                                            

test_APIs/test_html_report.py::test_w1 test_w1
PASSED
test_APIs/test_html_report.py::test_w2 test_w2
PASSED
test_APIs/test_html_report.py::test_w3 test_w3
PASSED

---------- generated html file: file://F:\Development\Trials\tPytest1\report.html -----------
===================================== 3 passed in 0.13s =====================================
PS F:\Development\Trials\tPytest1> ls


    目录: F:\Development\Trials\tPytest1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2021/8/18     13:42                .idea
d-----         2021/8/18     11:41                .pytest_cache
d-----         2021/8/18     13:44                test_APIs
d-----         2021/8/18     11:55                __pycache__
-a----         2021/8/18     11:57            155 apytest.ini
-a----         2021/8/18     13:46          15328 report.html


PS F:\Development\Trials\tPytest1>

```

