# pytest-xdist

```py
# encoding: utf-8
import time

import pytest


class TestMultiThread(object):

    def test_mt_01(self):
        n = 2
        time.sleep(n)
        print(f"Sleep {n}")

    def test_mt_02(self):
        n = 3
        time.sleep(n)
        print(f"Sleep {n}")

    def test_mt_03(self):
        n = 2
        time.sleep(n)
        print(f"Sleep {n}")

    def test_mt_04(self):
        n = 4
        time.sleep(n)
        print(f"Sleep {n}")

    def test_mt_05(self):
        n = 2
        time.sleep(n)
        print(f"Sleep {n}")

```

```
PS F:\Development\Trials\tPytest> pytest.exe .\test_case\test_multithread.py -v -s -n 5
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\users\\envs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.17134-SP0', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.40', 'forked': '1.3.0', 'html': '3.1.1', 'metadata': '1.11.0'
, 'xdist': '2.2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2'}
rootdir: F:\Development\Trials\tPytest
plugins: allure-pytest-2.8.40, forked-1.3.0, html-3.1.1, metadata-1.11.0, xdist-2.2.1
[gw0] win32 Python 3.8.5 cwd: F:\Development\Trials\tPytest
[gw1] win32 Python 3.8.5 cwd: F:\Development\Trials\tPytest
[gw2] win32 Python 3.8.5 cwd: F:\Development\Trials\tPytest
[gw3] win32 Python 3.8.5 cwd: F:\Development\Trials\tPytest
[gw4] win32 Python 3.8.5 cwd: F:\Development\Trials\tPytest
[gw0] Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
[gw1] Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
[gw2] Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
[gw3] Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
[gw4] Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
gw0 [5] / gw1 [5] / gw2 [5] / gw3 [5] / gw4 [5]
scheduling tests via LoadScheduling

test_case/test_multithread.py::TestMultiThread::test_mt_02
test_case/test_multithread.py::TestMultiThread::test_mt_04
test_case/test_multithread.py::TestMultiThread::test_mt_01
test_case/test_multithread.py::TestMultiThread::test_mt_05
test_case/test_multithread.py::TestMultiThread::test_mt_03
[gw4] PASSED test_case/test_multithread.py::TestMultiThread::test_mt_05
[gw0] PASSED test_case/test_multithread.py::TestMultiThread::test_mt_01
[gw2] PASSED test_case/test_multithread.py::TestMultiThread::test_mt_03
[gw1] PASSED test_case/test_multithread.py::TestMultiThread::test_mt_02
[gw3] PASSED test_case/test_multithread.py::TestMultiThread::test_mt_04

=========================================================================================================== 5 passed in 6.00s ============================================================================================================
PS F:\Development\Trials\tPytest>

```
