
## Supported Pytest features
Some of the common Pytest features that the Allure report supports include xfails, fixtures and finalizers, marks, conditional skips and parametrization.

Allure 报表支持的一些常见 Pytest 特性包括 xfails, fixtures and finalizers, marks, conditional skips and parametrization.


### Xfail
这是标记预期失败的pytest方法：（pytest docs）

```py
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True
```




### Conditional mark
在Pytest中，您可以有条件地将测试标记为在某些特定条件下不执行（Pytest文档）：

```py
@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass
```
当条件求值为true时，test将从装饰器接收报告中的 “Skipped” 状态、标记和描述。



### Fixtures and Finalizers

fixture和finalizer是Pytest将分别在测试开始之前和测试结束之后调用的实用函数。Allure跟踪每个fixture的调用，并详细显示调用了哪些方法和哪些参数，保留了正确的调用顺序

你不需要标记你的 fixture，使他们在报告中可见，他们将自动检测到不同的skope。

```py
@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        function_scope_step()
    request.addfinalizer(function_scope_finalizer)


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        class_scope_step()
    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        module_scope_step()
    request.addfinalizer(module_finalizer_fixture)


@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        session_scope_step()
    request.addfinalizer(session_finalizer_fixture)


class TestClass(object):

    def test_with_scoped_finalizers(self,
                                    function_scope_fixture_with_finalizer,
                                    class_scope_fixture_with_finalizer,
                                    module_scope_fixture_with_finalizer,
                                    session_scope_fixture_with_finalizer):
        step_inside_test_body()
```


根据fixture执行的结果，依赖于fixture的测试可能会收到不同的状态。fixture中的异常将使所有依赖测试中断，pytest.skip（）调用将使所有依赖测试跳过。


```py
import pytest

@pytest.fixture
def skip_fixture():
    pytest.skip()


@pytest.fixture
def fail_fixture():
    assert False


@pytest.fixture
def broken_fixture():
    raise Exception("Sorry, it's broken.")


def test_with_pytest_skip_in_the_fixture(skip_fixture):
    pass


def test_with_failure_in_the_fixture(fail_fixture):
    pass


def test_with_broken_fixture(broken_fixture):
    pass
```




### Parametrization

您可以使用 @pytest.mark.parametrize 从输入参数集生成许多测试用例

所有参数名称和值都将被捕获到报告中，并且可以选择将参数名称替换为ids kwarg中提供的字符串描述。


```py
import allure
import pytest


@allure.step
def simple_step(step_param1, step_param2 = None):
    pass


@pytest.mark.parametrize('param1', [True, False], ids=['id explaining value 1', 'id explaining value 2'])
def test_parameterize_with_id(param1):
    simple_step(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step(param1, param2)


@pytest.mark.parametrize('param1', [True], ids=['boolean parameter id'])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
@pytest.mark.parametrize('param3', [1])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step(param1, param3)
    simple_step(param2)
```


