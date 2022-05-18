# pytest-xdist 多进程并发

当测试用例非常多的时候，一条条按顺序执行测试用例，是很浪费测试时间的。这时候就可以用到 pytest-xdist，让自动化测试用例可以分布式执行，从而大大节省测试时间。

pytest-xdist 是属于进程级别的并发。

分布式测试用例的设计原则：
1. 独立运行：用例之间是独立的，并且没有依赖关系，还可以完全独立运行。
2. 随机执行：用例执行不强制按顺序执行，支持顺序执行或随机执行。
3. 不影响其他用例：每个用例都能重复运行，运行结果不会影响其他用例。

pytest-xdist 通过一些独特的测试执行模式扩展了 pytest：
1. 测试运行并行化：如果有多个CPU或主机，则可以将它们用于组合的测试运行。这样可以加快开发速度或使用远程计算机的特殊资源。
2. --looponfail：在子进程中重复运行测试。每次运行之后，pytest 都会等到项目中的文件更改后再运行之前失败的测试。重复此过程，直到所有测试通过，然后再次执行完整运行。
3. 跨平台覆盖：可以指定不同的 Python 解释器或不同的平台，并在所有这些平台上并行运行测试。

## 安装
在命令行中运行以下命令进行安装：
```
pip install pytest-xdist
```
或者（使用国内的豆瓣源，数据会定期同步国外官网，速度快。）
```
pip install pytest-xdist -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```


## 原理和流程
xdist 的分布式类似于一主多从的结构，master 机负责下发命令，控制 slave 机；slave 机根据 master 机的命令执行特定测试任务。

在 xdist 中，主是 master，从是 workers。

### 分布式测试的原理：
1. xdist 会产生一个或多个 workers，workers 都通过 master 来控制；
2. 每个 worker 负责执行完整的测试用例集，然后按照 master 的要求运行测试，而 master 机不执行测试任务。

### 分布式测试的流程：

1. 创建 worker
   1. master 会在总测试会话（test session）开始前产生一个或多个 worker；
   2. master 和 worker 之间是通过 execnet 和网关来通信的；
   3. 实际编译执行测试代码的 worker 可能是本地机器也可能是远程机器。

2. 收集测试用例
   1. 每个 worker 类似一个迷你型的 pytest 执行器；
   2. worker 会执行一个完整的 test collection 过程（收集所有测试用例的过程）；
   3. 然后把测试用例的 ids 返回给 master；
   4. master 是不会执行任何测试用例集的。

    注：所以为什么脚本代码里有打印语句（print）通过分布式测试时结果没有输出用例的打印内容，因为主机并不执行测试用例，PyCharm 相当于一个 master。

3. master 检测 workers 收集到的测试用例集
   1. master 接收到所有 worker 收集的测试用例集之后，master 会进行一些完整性检查，以确保所有 worker 都收集到一样的测试用例集（包括顺序）；
   2. 如果检查通过，会将测试用例的 ids 列表转换成简单的索引列表，每个索引对应一个测试用例的在原来测试集中的位置；
   3. 所有的节点都保存着相同的测试用例集，并且使用这种方式可以节省带宽，因为 master 只需要告知 workers 需要执行的测试用例对应的索引，而不用告知完整的测试用例信息。

4. 测试用例分发 --dist-mode 选项
   1. each：master 将完整的测试索引列表分发到每个 worker。
   2. load：master 将大约25%的测试用例以轮询的方式分发到各个 worker，剩余的测试用例则会等待 workers 执行完测试用例以后再分发。

    注：可以使用 pytest_xdist_make_scheduler 这个 hook 来实现自定义测试分发逻辑。

5. 测试用例的执行
   1. workers 重写了 pytest_runtestloop（pytest 的默认实现是循环执行所有在 test session 这个对象里面收集到的测试用例）；
   2. 但是在 xdist 里, workers 实际上是等待 master 为其发送需要执行的测试用例；
   3. 当 worker 收到测试任务, 就顺序执行 pytest_runtest_protocol；
   4. 值得注意的一个细节是：workers 必须始终保持至少一个测试用例在任务队列里, 以兼容 pytest_runtest_protocol(item, nextitem)hook 的参数要求，为了将 nextitem 传给 hook；
   5. worker 会在执行最后一个测试项前等待 master 的更多指令；
   6. 如果它收到了更多测试项, 那么就可以安全的执行 pytest_runtest_protocol，因为这时 nextitem 参数已经可以确定；
   7. 如果它收到一个 "shutdown" 信号, 那么就将 nextitem 参数设为 None, 然后执行 pytest_runtest_protocol。

6. 测试用例再分发 --dist-mode=load
   1. 当 workers 开始/结束执行时，会把测试结果返回给 master，这样其他 pytest hook 比如（pytest_runtest_protocol 和 pytest_runtest_protocol 就可以正常执行）；
   2. master 在 worker 执行完一个测试后，基于测试执行时长以及每个 work 剩余测试用例综合决定是否向这个 worker 发送更多的测试用例。

7. 测试结束
   1. 当 master 没有更多执行测试任务时，它会发送一个 "shutdown" 信号给所有 worker；
   2. 当 worker 将剩余测试用例执行完后退出进程；
   3. master 等待所有 worker 全部退出；
   4. 此时仍需要处理诸如 pytest_runtest_logreport 等事件。





## 实例

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







## ref
* [版权声明：本文为CSDN博主「wangmcn」的原创文章，遵循CC](https://blog.csdn.net/wangmcn/article/details/121080902)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

