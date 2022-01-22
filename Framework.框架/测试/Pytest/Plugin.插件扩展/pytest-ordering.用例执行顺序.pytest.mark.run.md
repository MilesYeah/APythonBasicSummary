# Pytest系列 - 用例的执行顺序

前言

pytest默认按字母顺序去执行的（小写英文--->大写英文--->0-9数字）
用例之间的顺序是文件之间按照ASCLL码排序，文件内的用例按照从上往下执行。
1. setup_module
2. setup_claas
3. setup_function
4. testcase
5. teardown_function
6. teardown_claas
7. teardown_module

可以通过第三方插件pytest-ordering实现自定义用例执行顺序
[官方文档：](https://pytest-ordering.readthedocs.io/en/develop/)

注意：一旦设置了自定义的执行顺序，就必须得衍生 @pytest.mark.run(order=1) 里面得order字段



## 代码实现
### 安装插件
```
pip install pytest-ordering
```
### 代码
为了演示，新建了个项目，目录结构。
新建用例必须严格遵守pytest的规范创建。

```py
# test_login.py
def test_login02():
    assert 1 == 1

def test_login01():
    assert True

# test_project.py
def test_01():
    assert True

# test_three.py
def test_02():
    assert True
```



### 执行结果
用例执行顺序：test_three.py > testLogin/test_login.py > testProject/test_project
在.py文件内是从上往下执行，不管大小排序。


### 改变用例执行顺序
#### 方式一

1. 第一个执行 `@pytest.mark.first`
2. 第二个执行 `@pytest.mark.second`
3. 倒数第二个执行 `@pytest.mark.second_to_last`
4. 最后一个执行`@pytest.mark.last`

#### 方式二

1. 第一个执行 `@pytest.mark.run('first')`
2. 第二个执行 `@pytest.mark.run('second')`
3. 倒数第二个执行 `@pytest.mark.run('second_to_last')`
4. 最后一个执行 `@pytest.mark.run('last')`

#### 方式三

1. 第一个执行 `@pytest.mark.run(order=1)`
2. 第二个执行 `@pytest.mark.run(order=2)`
3. 倒数第二个执行 `@pytest.mark.run(order=-2)`
4. 最后一个执行 `@pytest.mark.run(order=-1)`

以上三种方式可以自行尝试，以下情况需要特别注意，我们就那上面的文件举例说明。
```py
# test_login.py
@pytest.mark.run(order=1)
def test_login02():
    assert 1 == 1

@pytest.mark.run(order=2)
def test_login01():
    assert True

# test_project.py
@pytest.mark.run(order=1)
def test_01():
    assert True

# test_three.py
def test_02():
    assert True
```

已经改变了用例执行规则，针对于是全局的，会先执行完@pytest.mark.run(order=1)才会执行order=2的用例

其实总体来说，这个插件的实用场景不是很多，如果需要指定某个用例第一个执行和最后执行，可以用该插件实现。

如果要按照你指定的顺序执行下去，需要在每个用例前都加上@pytest.mark.run(order=1)，其中order中的数字需递增。







## 实例

### pytest-ordering
Pytest 默认按照用例的定义顺序执行，不是按照编号
* `@pytest.mark.run(order=1)` 可以通过 order 指定执行顺序，使用 order 我们需要先安装 `pytest-ordering`
* 

```py
import time

import pytest


class TestOrdering(object):

    def test_05(self):
        n = 2
        print(f"Sleep {n}")

    def test_01(self):
        n = 2
        print(f"Sleep {n}")

    @pytest.mark.run(order=1)
    def test_02(self):
        n = 3
        print(f"Sleep {n}")

    def test_03(self):
        n = 2
        print(f"Sleep {n}")

    def test_04(self):
        n = 4
        print(f"Sleep {n}")
```


```
PS F:\Development\Trials\tPytest> pytest.exe -v .\test_case\test_ordering.py
========================================================================================================== test session starts ===========================================================================================================
platform win32 -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\users\\envs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.17134-SP0', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.40', 'base-url': '1.4.2', 'forked': '1.3.0', 'html': '3.1.1',
 'metadata': '1.11.0', 'ordering': '0.6', 'rerunfailures': '9.1.1', 'selenium': '2.0.1', 'variables': '1.9.0', 'xdist': '2.2.1'}, 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk-12.0.2', 'Base URL': '', 'Driver': None, 'Capabilities': {}}
sensitiveurl: .*
rootdir: F:\Development\Trials\tPytest
plugins: allure-pytest-2.8.40, base-url-1.4.2, forked-1.3.0, html-3.1.1, metadata-1.11.0, ordering-0.6, rerunfailures-9.1.1, selenium-2.0.1, variables-1.9.0, xdist-2.2.1
collected 5 items                                                                                                                                                                                                                         

test_case/test_ordering.py::TestOrdering::test_02 PASSED                                                                                                                                                                            [ 20%]
test_case/test_ordering.py::TestOrdering::test_05 PASSED                                                                                                                                                                            [ 40%]
test_case/test_ordering.py::TestOrdering::test_01 PASSED                                                                                                                                                                            [ 60%]
test_case/test_ordering.py::TestOrdering::test_03 PASSED                                                                                                                                                                            [ 80%]
test_case/test_ordering.py::TestOrdering::test_04 PASSED                                                                                                                                                                            [100%]

=========================================================================================================== 5 passed in 0.10s ============================================================================================================
PS F:\Development\Trials\tPytest>
```



### 实例 2

```py
import pytest


class TestOrder():

    @pytest.mark.run(order=3)
    def test_o1(self):
        print("test O1")

    @pytest.mark.run(order=1)
    def test_o2(self):
        print("test O4")

    @pytest.mark.run(order=2)
    def test_o3(self):
        print("test O3")

    @pytest.mark.run(order=4)
    def test_o4(self):
        print("test O4")


if __name__ == '__main__':
    pytest.main()

```


```sh
C:\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Development/Trials/tPytest1/test_APIs/test_mark_order.py
Testing started at 19:38 ...
Launching pytest with arguments F:/Development/Trials/tPytest1/test_APIs/test_mark_order.py --no-header --no-summary -q in F:\Development\Trials\tPytest1\test_APIs

============================= test session starts =============================
collecting ... collected 4 items

test_mark_order.py::TestOrder::test_o2 
test_mark_order.py::TestOrder::test_o3 
test_mark_order.py::TestOrder::test_o1 
test_mark_order.py::TestOrder::test_o4 

============================== 4 passed in 0.14s ==============================

Process finished with exit code 0
PASSED                            [ 25%]test O4
PASSED                            [ 50%]test O3
PASSED                            [ 75%]test O1
PASSED                            [100%]test O4

```

