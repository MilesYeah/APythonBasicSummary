

allure是一个轻量级灵活的支持多语言的测试报告工具，java语言开发，支持pytest, javascript, php, ruby等，也可以集成到jenkins，在pycharm中我们需要安装allure-pytest(或者pip install allure-pytest)


| 命令                                                    | 描述                                                         |
| ------------------------------------------------------- | ------------------------------------------------------------ |
| `pytest test1.py --alluredir=./result/`                 | 执行test1.py中的测试用例，将allure数据存放在 result 文件夹中 |
| `pytest test1.py --allure-features=“结算模块”`          | 只执行“结算模块”的测试用例                                   |
| `pytest test1.py --allure-stories=“结算模块第二条用例”` | 只执行“结算模块第二条用例”                                   |
| `pytest test1.py --allure-features=“加购模块”`          | 只运行“加购模块”                                             |
| `pytest test1.py --allure-severities="normal,critical"` | 执行allure级别为 normal和critical的用例                      |
| `allure serve ./result/`                                | 唤起浏览器展示 result 文件夹中的数据                         |
| `allure generate ./result1`                             | 将result1中的数据转换为allure报告，存放在allure-report文件夹 |
| `allure generate ./result1 -o report`                   | 指定转换报告存放文件夹                                       |
|                                                         |                                                              |



```py
import os

import pytest


# 如何运行

if __name__ == "__main__":
    # 生成 html 报告
    pytest.main(['../test_case/', '--html=../report/simple_html.html', '--junitxml=../report/report.junit.xml', '--alluredir', '../report/allure_data'])
    os.system('allure generate ../report/allure_data/ -o ../report/allure_html/ --clean')
    # os.chdir('../report/allure_html/')
    # os.system('start index.html')
```







## ref
* [原文链接：](https://blog.csdn.net/qq_41780297/article/details/114214694)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

