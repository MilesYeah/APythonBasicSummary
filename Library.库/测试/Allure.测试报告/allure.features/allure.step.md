# allure.step

@allure.step 
* allure报告最重要的一点是，它允许对每个测试用例进行非常详细的步骤说明
* 通过 @allure.step() 装饰器，可以让测试用例在allure报告中显示更详细的测试过程

知识点
1. step() 只有一个参数，就是title，你传什么，在allure上就显示什么
2. 可以像python字符串一样，支持位置参数和关键字参数 {0}，{arg2}，可看第四步那里，如果函数的参数没有匹配成功就会报错哦
3. step() 的使用场景，给我感觉就是，当方法之间嵌套会比较有用，否则的话只会显示一个步骤


## Steps

Allure 报告的第一个也是可能最重要的方面是，它允许获得每个测试调用的非常详细的逐步表示。这可以通过@allure.step 装饰器实现，该装饰器使用提供的参数向报表中添加对带注释的方法或函数的调用。

用@step注释的方法可以存储在测试之外，并在需要时导入。Step方法可以具有任意深度的嵌套结构。

```py
import allure
import pytest

from .steps import imported_step


@allure.step
def passing_step():
    pass


@allure.step
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_imported_step():
    passing_step()
    imported_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
```
每个步骤的状态都显示在名称右侧的一个小图标中。嵌套的步骤被组织成树状的可折叠结构。



## 带参数的 step

```py
import allure


@allure.step("第一步")
def passing_step():
    pass


@allure.step("第二步")
def step_with_nested_steps():
    nested_step()


@allure.step("第三步")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("第四步{0}，{arg2}")
def nested_step_with_arguments(arg1, arg2):
    pass

```



## 嵌套的 steps 和 带参数的 step
@allure.streps 可以有一个描述行，该行支持传递的位置参数和关键字参数的占位符。关键字参数的默认参数也将被捕获。

```py
import allure

@allure.step('Step with placeholders in the title, positional: "{0}", keyword: "{key}"')
def step_with_title_placeholders(arg1, key=None):
    pass


def test_steps_with_placeholders():
    step_with_title_placeholders(1, key='something')
    step_with_title_placeholders(2)
    step_with_title_placeholders(3, 'anything')
```



## Steps 在 fixtures 中也是支持的。

下面是一个使用conftest.py模块中定义的fixture的测试示例（这样的fixture即使没有直接导入，也将由Pytest解析）：

```py
# conftest.py
import allure
import pytest


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_with_conftest_step():
    conftest_step()
import allure

from .steps import imported_step


@allure.step
def passing_step():
    pass


def test_with_step_in_fixture_from_conftest(fixture_with_conftest_step):
    passing_step()
```

fixture 中的 step 显示在单独的树中，用于 setup 和 teardown。





## ref
* [Pytest系列（20）- allure的特性，@allure.step()、allure.attach的详细使用 ](https://www.cnblogs.com/poloyy/p/12716659.html)
* []()
* []()
* []()
* []()
* []()
* []()
