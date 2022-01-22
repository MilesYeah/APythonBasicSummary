# allure.description

可以添加足够详细的测试用例描述，以便于管理层查看


您可以添加测试的详细描述，以便为报表读取器提供所需的上下文。这可以通过几种方式实现：

1. @allure.description
   1. 您可以添加 @allure.description 装饰器来提供描述字符串
2. @allure.description_html
   1. 您可以使用 @allure.description_html 提供一些html，以便在测试用例的“description”部分中呈现。
3. 自动提取 docstring 将其作为 description 填写在测试报告中
4. @allure.dynamic.description 
   1. 从测试体内部动态更新描述。
5. Alternatively description 
   1. 将简单地从测试方法的docstring中提取。



## @allure.description

```py
@allure.description("""
Multiline test description.
That comes from the allure.description decorator.

Nothing special about it.
""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)


@allure.description("""
这是一个@allure.description装饰器
没有特别的用处
""")
def test_description_from_decorator():
    assert 42 == int(6 * 7)
```



## @allure.description_html

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

```



## 自动提取 docstring
```py
def test_unicode_in_docstring_description():
    """Unicode in description.

    Этот тест проверяет юникод.

    你好伙计.
    """
    assert 42 == int(6 * 7)


def test_unicode_in_docstring_description():
    """
    当然，在方法声明的下一行这样子写，也算一种添加description的方式哦
    """
    assert 42 == int(6 * 7)

```



## @allure.dynamic.description 

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


