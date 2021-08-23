# pytest.mark.usefixtures
[URL pytest.mark.usefixtures](https://docs.pytest.org/en/stable/reference.html#pytest.mark.usefixtures)

有时测试函数不需要直接访问fixture对象。例如，测试可能需要使用一个空目录作为当前工作目录，但不关心具体目录。

下面是如何使用标准tempfile和pytest fixture来实现它。我们将装饰器的创建分离到conftest.py文件中：

```py
# conftest.py

import os
import shutil
import tempfile

import pytest


@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)
```

并通过 UseFixture 标记声明其在测试模块中的使用：

```py
# test_setenv.py
import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```


由于usefixtures标记，每个测试方法的执行都需要cleandir fixture，就像您为每个方法指定了“cleandir”函数参数一样。让我们运行它来验证我们的夹具是否激活，测试是否通过：

```
$ pytest -q
..                                                                   [100%]
2 passed in 0.12s
```





## 指定多个装置

```py
@pytest.mark.usefixtures("cleandir", "anotherfixture")
def test():
    ...
```





## pytestmark 测试模块级别指定 fixture
您可以使用 pytestmark 在测试模块级别指定 fixture 用法：

```py
pytestmark = pytest.mark.usefixtures("cleandir")
```

也可以将项目中所有测试所需的装置放入ini文件中：

```ini
# content of pytest.ini
[pytest]
usefixtures = cleandir
```





## fixture 上使用其他 fixture 将无效

注意：此标记在夹具功能中不起作用。例如，这将无法按预期工作：

```py
@pytest.mark.usefixtures("my_other_fixture")
@pytest.fixture
def my_fixture_that_sadly_wont_use_my_other_fixture():
    ...
```

目前，这不会产生任何错误或警告，但这将由#3664处理。

