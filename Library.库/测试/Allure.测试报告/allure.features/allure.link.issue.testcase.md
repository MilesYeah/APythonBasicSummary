# allure.link.issue.testcase

要将报表与 bug 跟踪系统或测试管理系统集成，Allure有以下描述符：
1. @allure.link, 
2. @allure.issue
3. @allure.testcase

知识点
* issue()和testcase()其实调用的也是link()，`只是link_type不一样`
* 必传参数 url：跳转的链接
* 可选参数 name：显示在allure报告的名字，如果不传就是显示完整的链接；`建议传！！不然可读性不高`
  * 不传name的话，如果链接很长，可读性就比较差啦！ 
  * 传name，写好链接描述，就知道这个链接是干嘛的，反正三个装饰器的作用都是一样的，就是样式略微不同.....
* 可以理解成：三个方法是一样的，我们都提供跳转链接和名字，只是链接的type不一样，最终显示出来的`样式不一样而已【type不一样，样式不一样】`
* 如果你喜欢，只用@allure.link()也可以
  * 为了减少程序的阅读复杂性，其实可以统一用@allure.link()
* 而出现三个装饰器的原因是为了更好地将`链接分类【访问连接、Bug链接、测试用例链接】`

```py
class LinkType(object):
    LINK = 'link'
    ISSUE = 'issue'
    TEST_CASE = 'test_case'
```

源码
```py
def link(url, link_type=LinkType.LINK, name=None):
    return safely(plugin_manager.hook.decorate_as_link(url=url, link_type=link_type, name=name))


def issue(url, name=None):
    return link(url, link_type=LinkType.ISSUE, name=name)


def testcase(url, name=None):
    return link(url, link_type=LinkType.TEST_CASE, name=name)
```


## 示例
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



## @allure.link 
将在“链接”部分提供指向所提供url的可单击链接：



## @allure.issue 
将提供一个带有小错误图标的链接。此描述符将测试用例 id 作为输入参数，以将其与为问题链接类型提供的链接模板一起使用。链接模板在 Pytest 的 `--allure-link-pattern` 配置选项中指定。必须使用冒号指定链接模板和类型：

```
$ pytest directory_with_tests/ --alluredir=/tmp/my_allure_report  --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
```


模板关键字是 issue、 link 和 test_case ，为相应类型的链接提供模板。


