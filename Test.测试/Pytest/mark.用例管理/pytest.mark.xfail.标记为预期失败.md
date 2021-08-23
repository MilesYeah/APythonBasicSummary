# pytest.mark.xfail 将测试函数标记为预期失败
[URL pytest.mark.xfail](https://docs.pytest.org/en/stable/reference.html#pytest.mark.xfail)


可以使用xfail标记来指示您希望测试失败：

```py
@pytest.mark.xfail
def test_function():
    ...
```

此测试将运行，但失败时不会报告回溯。相反，终端报告将在“预期失败”（XFAIL）或“意外通过”（XPASS）部分列出它。


### 显式标注 xfail
或者，也可以在测试或其设置函数中强制将测试标记为XFAIL：
```py
def test_function():
    if not valid_config():
        pytest.xfail("failing configuration (but should work)")
def test_function2():
    import slow_module

    if slow_module.slow_function():
        pytest.xfail("slow_module taking too long")
```

这两个例子说明了您不想在模块级别检查条件的情况，也就是说，如果不是这样，条件将被评估为标记。


这将使test_函数XFAIL。请注意，在pytest.xfail（）调用之后不会执行其他代码，这与标记不同。这是因为它是通过引发一个已知的异常在内部实现的。


### condition  条件参数
如果预期测试仅在某个条件下失败，则可以通过该条件作为第一个参数：

```py
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_function():
    ...
```

请注意，还必须传递一个原因（请参见pytest.mark.xfail中的参数描述）。


### reason parameter
可以使用reason参数指定预期失败的动机：

```py
@pytest.mark.xfail(reason="known parser issue")
def test_function():
    ...
```

### raises parameter
如果您想更具体地说明测试失败的原因，可以在raises参数中指定一个异常或一个异常元组。

```py
@pytest.mark.xfail(raises=RuntimeError)
def test_function():
    ...
```

如果测试失败，则该测试将被报告为常规失败，除非本节未提及异常。


### run parameter
如果测试应标记为xfail并报告为xfail，但甚至不应执行，请将run参数用作False：

```py
@pytest.mark.xfail(run=False)
def test_function():
    ...
```

这对于正在使解释器崩溃的xfailing测试特别有用，应该稍后进行研究。


### strict parameter
默认情况下，XFAIL和XPASS都不会使测试套件失败。您可以通过将strict keyword only参数设置为True来更改此设置：

```py
@pytest.mark.xfail(strict=True)
def test_function():
    ...
```

这将使这个测试的XPASS（“意外通过”）结果使测试套件失败。


您可以使用xfail_strict ini选项更改strict参数的默认值：

```ini
[pytest]
xfail_strict=true
```

### Ignoring xfail
通过在命令行上指定：

```
pytest --runxfail
```

您可以强制运行和报告xfail标记的测试，就好像它根本没有被标记一样。这也会导致 pytest.xfail（） 不产生任何效果。


### 示例

```py
import pytest

xfail = pytest.mark.xfail


@xfail
def test_hello():
    assert 0


@xfail(run=False)
def test_hello2():
    assert 0


@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0


@xfail(reason="bug 110")
def test_hello4():
    assert 0


@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0


def test_hello6():
    pytest.xfail("reason")


@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1
```

### 带参数化的Skip/xfail

使用参数化时，可以将skip和xfail等标记应用于单个测试实例：
```py
import pytest


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected
```


