# pytest-dependency 控制用例的依赖关系

```
pip install pytest-dependency
```

```py
@pytest.mark.dependency(depends=[依赖的测试用例名称])
```





## 实例
比如说测试用例C对测试用例A和测试用例B都有依赖关系，我们希望只有当测试用例A和测试用例B都执行通过后，才去执行C，否则跳过C

### C依赖AB，但是A挂掉，B正确
假设测试用例D也依赖与测试用例A

当测试用例A失败的时候，测试用例C和测试用例D都会直接跳过，如下：

```py
import pytest

class Test_A():

    @pytest.mark.dependency()
    def test_case_a(self):
        print(f"测试用例A")
        assert 2 > 5

    @pytest.mark.dependency()
    def test_case_b(self):
        print(f"测试用例B")
        assert 2 > 0

    @pytest.mark.dependency(depends=['test_case_a', 'test_case_b'])
    def test_case_c(self):
        print(f"测试用例C")
        assert 28 > 12

    @pytest.mark.dependency(depends=['test_case_a'])
    def test_case_d(self):
        print(f"测试用例D")
        assert 28 > 12

    def test_case_e(self):
        print(f"测试用例E")
        assert 28 > 12
```

运行结果如下：

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tPytestDependency.py
Testing started at 18:40 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tPytestDependency.py --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest\tFixture

============================= test session starts =============================
collecting ... collected 5 items

tPytestDependency.py::Test_A::test_case_a FAILED                         [ 20%]测试用例A

tPytestDependency.py:4 (Test_A.test_case_a)
self = <tPytest.tFixture.tPytestDependency.Test_A object at 0x0000025041C38D30>

    @pytest.mark.dependency()
    def test_case_a(self):
        print(f"测试用例A")
>       assert 2 > 5
E       assert 2 > 5

tPytestDependency.py:8: AssertionError
PASSED                         [ 40%]测试用例B
SKIPPED (test_case_c depen...) [ 60%]
Skipped: test_case_c depends on test_case_a
SKIPPED (test_case_d depen...) [ 80%]
Skipped: test_case_d depends on test_case_a
PASSED                         [100%]测试用例E



tPytestDependency.py::Test_A::test_case_b 
tPytestDependency.py::Test_A::test_case_c 
tPytestDependency.py::Test_A::test_case_d 
tPytestDependency.py::Test_A::test_case_e 

=================== 1 failed, 2 passed, 2 skipped in 0.47s ====================

Process finished with exit code 1

```

```py

```


### C依赖AB，但是B挂掉，A正确

当测试用例A运行通过，测试用例B运行不通过的时候，测试用例C运行不会通过，测试用例D和测试用例E运行通过，如下：
```py
import pytest

class Test_A():

    @pytest.mark.dependency()
    def test_case_a(self):
        print(f"测试用例A")
        assert 6 > 5

    @pytest.mark.dependency()
    def test_case_b(self):
        print(f"测试用例B")
        assert 2 > 7

    @pytest.mark.dependency(depends=['test_case_a', 'test_case_b'])
    def test_case_c(self):
        print(f"测试用例C")
        assert 28 > 12

    @pytest.mark.dependency(depends=['test_case_a'])
    def test_case_d(self):
        print(f"测试用例D")
        assert 28 > 12

    def test_case_e(self):
        print(f"测试用例E")
        assert 28 > 12
```

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --target tPytestDependency2.py::Test_A
Testing started at 18:43 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments tPytestDependency2.py::Test_A --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest\tFixture

============================= test session starts =============================
collecting ... collected 5 items

tPytestDependency2.py::Test_A::test_case_a 
tPytestDependency2.py::Test_A::test_case_b PASSED                        [ 20%]测试用例A
FAILED                        [ 40%]测试用例B

tPytestDependency2.py:9 (Test_A.test_case_b)
self = <tPytest.tFixture.tPytestDependency2.Test_A object at 0x0000024DDC83D570>

    @pytest.mark.dependency()
    def test_case_b(self):
        print(f"测试用例B")
>       assert 2 > 7
E       assert 2 > 7

tPytestDependency2.py:13: AssertionError
SKIPPED (test_case_c depe...) [ 60%]
Skipped: test_case_c depends on test_case_a
SKIPPED (test_case_d depe...) [ 80%]
Skipped: test_case_d depends on test_case_a
PASSED                        [100%]测试用例E



tPytestDependency2.py::Test_A::test_case_c 
tPytestDependency2.py::Test_A::test_case_d 
tPytestDependency2.py::Test_A::test_case_e 

=================== 1 failed, 2 passed, 2 skipped in 0.44s ====================

Process finished with exit code 1

```

```py

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

