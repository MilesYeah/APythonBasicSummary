# pytest.mark.filterwarnings 为标记的测试项添加警告筛选器
[URL pytest.mark.filterwarnings](https://docs.pytest.org/en/stable/reference.html#pytest.mark.filterwarnings)


`pytest.mark.filterwarnings(filter)`
* filter (str) – 警告规范字符串，由元组（action、message、category、module、lineno）的内容组成，如Python文档的Warnings filter部分所指定，用“：”分隔。可选字段可以省略。传递给筛选的模块名不是regex转义的。

```py
@pytest.mark.filterwarnings("ignore:.*usage will be deprecated.*:DeprecationWarning")
def test_foo():
    ...
```










