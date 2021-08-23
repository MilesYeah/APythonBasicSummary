# Allure Features

Allure 目前支持几乎所有可用的功能，除了Pytest环境。

1. @allure.feature('×××')   #一级分层
2. @allure.story('×××')   #二级分层
3. @allure.title("This test has a custom title")
4. @allure.step
5. Description
   1. @allure.description
   2. @allure.description_html
   3. @allure.dynamic.description 
   4. Alternatively description 
6. Links
   1. @allure.link, 提供指向所提供url的可单击链接
   2. @allure.issue 提供一个带有小错误图标的链接
   3. @allure.testcase
7.  Attachment
   1. allure.attach(body, name, attachment_type, extension):
   2. allure.attach.file(source, name, attachment_type, extension):


![](pics/../allure.feature.simple.png)
![](pics/../allure.feature.png)


## Feature



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



### 嵌套的 steps 和 带参数的 step
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


### Steps 在 fixtures 中也是支持的。

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



## Attachments

报告可以显示许多不同类型的附件，这些附件可以补充测试、step 或 fixture 结果。可以通过调用如下方法添加 attachment：

### allure.attach(body, name, attachment_type, extension):
1. body
   1. 要写入文件的原始内容。
2. name
   1. 包含文件名的字符串
3. attachment_type
   1. 其中一个allure.attachment_type值 。 
   2. 支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML
4. extension
   1. 提供的将用作创建文件的扩展名

### allure.attach.file(source, name, attachment_type, extension):
1. source
   1. 文件路径的字符串。
2. (other arguments are the same)


```py
import allure
import pytest


@pytest.fixture
def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('A text attacment in module scope fixture', 'blah blah blah', allure.attachment_type.TEXT)
    def finalizer_module_scope_fixture():
        allure.attach('A text attacment in module scope finalizer', 'blah blah blah blah', allure.attachment_type.TEXT)
    request.addfinalizer(finalizer_module_scope_fixture)


def test_with_attacments_in_fixture_and_finalizer(attach_file_in_module_scope_finalizer):
    pass


def test_multiple_attachments():
    allure.attach.file('./data/totally_open_source_kitten.png', attachment_type=allure.attachment_type.PNG)
    allure.attach('<head></head><body> a page </body>', 'Attach with HTML type', allure.attachment_type.HTML)
```


附件显示在它们所属的测试实体的上下文中。HTML类型的附件将呈现并显示在报告页上。这是一种方便的方法，可以为您自己的测试结果表示提供一些定制。



## Descriptions
您可以添加测试的详细描述，以便为报表读取器提供所需的上下文。这可以通过几种方式实现：

### @allure.description
您可以添加 @allure.description 装饰器来提供描述字符串


### @allure.description_html

您可以使用 @allure.description_html 提供一些html，以便在测试用例的“description”部分中呈现。


###  @allure.dynamic.description 
从测试体内部动态更新描述。


### Alternatively description 
将简单地从测试方法的docstring中提取。


```py
import allure

@allure.description_html("""
<h1>Test with some complicated html description</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr align="center">
    <td>William</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr align="center">
    <td>Vasya</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
""")
def test_html_description():
    assert True


@allure.description("""
Multiline test description.
That comes from the allure.description decorator.

Nothing special about it.
""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)


def test_unicode_in_docstring_description():
    """Unicode in description.

    Этот тест проверяет юникод.

    你好伙计.
    """
    assert 42 == int(6 * 7)
```


此外，还可以使用 @allure.dynamic.description 从测试体内部动态更新描述。

```py
import allure

@allure.description("""
This description will be replaced at the end of the test.
""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('A final description.')
```





## Titles

使用特定的 @allure.title 装饰器可以使测试 title 更具可读性。标题支持参数占位符并支持动态替换。

```py
import allure
import pytest


@allure.title("This test has a custom title")
def test_with_a_title():
    assert 2 + 2 == 4


@allure.title("This test has a custom title with unicode: Привет!")
def test_with_unicode_title():
    assert 3 + 3 == 6


@allure.title("Parameterized test title: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


@allure.title("This title will be replaced in a test body")
def test_with_dynamic_title():
    assert 2 + 2 == 4
    allure.dynamic.title('After a successful test finish, the title was replaced with this line.')
```




## Links
要将报表与 bug 跟踪系统或测试管理系统集成，Allure有以下描述符：
1. @allure.link, 
2. @allure.issue
3. @allure.testcase


```py
import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=Su5p2TqZxKU', name='Click me')
def test_with_named_link():
    pass


@allure.issue('140', 'Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    pass
```



### @allure.link 
将在“链接”部分提供指向所提供url的可单击链接：



### @allure.issue 
将提供一个带有小错误图标的链接。此描述符将测试用例 id 作为输入参数，以将其与为问题链接类型提供的链接模板一起使用。链接模板在 Pytest 的 `--allure-link-pattern` 配置选项中指定。必须使用冒号指定链接模板和类型：

```
$ pytest directory_with_tests/ --alluredir=/tmp/my_allure_report  --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
```


模板关键字是 issue、 link 和 test_case ，为相应类型的链接提供模板。


