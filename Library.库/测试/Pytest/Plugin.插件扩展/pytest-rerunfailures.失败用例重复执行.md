# pytest-rerunfailures

```py

import time

import pytest


class TestRerun(object):

    def test_rerun_01(self):
        n = 2
        print(f"Sleep {n}")
        assert n == 3

    def test_rerun_02(self):
        n = 3
        print(f"Sleep {n}")
        assert n == 2

    def test_rerun_03(self):
        n = 2
        print(f"Sleep {n}")

    def test_rerun_04(self):
        n = 4
        print(f"Sleep {n}")

    def test_rerun_05(self):
        n = 2
        print(f"Sleep {n}")

```


```
PS F:\Development\Trials\tPytest> pytest.exe .\test_case\test_rerun.py -vs --reruns 2
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\users\\envs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.17134-SP0', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.40', 'base-url': '1.4.2', 'forked': '1.3.0', 'html': '3.1.1',
 'metadata': '1.11.0', 'ordering': '0.6', 'rerunfailures': '9.1.1', 'selenium': '2.0.1', 'variables': '1.9.0', 'xdist': '2.2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2', 'Base URL': '', 'Driver': None, 'Capabilities': {}}
sensitiveurl: .*
rootdir: F:\Development\Trials\tPytest
plugins: allure-pytest-2.8.40, base-url-1.4.2, forked-1.3.0, html-3.1.1, metadata-1.11.0, ordering-0.6, rerunfailures-9.1.1, selenium-2.0.1, variables-1.9.0, xdist-2.2.1
collected 5 items                                                                                                                                                                                                                         

test_case/test_rerun.py::TestRerun::test_rerun_01 Sleep 2
RERUN
test_case/test_rerun.py::TestRerun::test_rerun_01 Sleep 2
RERUN
test_case/test_rerun.py::TestRerun::test_rerun_01 Sleep 2
FAILED
test_case/test_rerun.py::TestRerun::test_rerun_02 Sleep 3
RERUN
test_case/test_rerun.py::TestRerun::test_rerun_02 Sleep 3
RERUN
test_case/test_rerun.py::TestRerun::test_rerun_02 Sleep 3
FAILED
test_case/test_rerun.py::TestRerun::test_rerun_03 Sleep 2
PASSED
test_case/test_rerun.py::TestRerun::test_rerun_04 Sleep 4
PASSED
test_case/test_rerun.py::TestRerun::test_rerun_05 Sleep 2
PASSED

================================================================================================================ FAILURES ================================================================================================================
_______________________________________________________________________________________________________ TestRerun.test_rerun_01 _______________________________________________________________________________________________________

self = <tPytest.test_case.test_rerun.TestRerun object at 0x000001B45B11C040>

    def test_rerun_01(self):
        n = 2
        print(f"Sleep {n}")
>       assert n == 3
E       assert 2 == 3
E         +2
E         -3

test_case\test_rerun.py:18: AssertionError
_______________________________________________________________________________________________________ TestRerun.test_rerun_02 _______________________________________________________________________________________________________

self = <tPytest.test_case.test_rerun.TestRerun object at 0x000001B45B146100>

    def test_rerun_02(self):
        n = 3
        print(f"Sleep {n}")
>       assert n == 2
E       assert 3 == 2
E         +3
E         -2

test_case\test_rerun.py:23: AssertionError
======================================================================================================== short test summary info =========================================================================================================
FAILED test_case/test_rerun.py::TestRerun::test_rerun_01 - assert 2 == 3
FAILED test_case/test_rerun.py::TestRerun::test_rerun_02 - assert 3 == 2
================================================================================================== 2 failed, 3 passed, 4 rerun in 0.27s ==================================================================================================
PS F:\Development\Trials\tPytest>
```







