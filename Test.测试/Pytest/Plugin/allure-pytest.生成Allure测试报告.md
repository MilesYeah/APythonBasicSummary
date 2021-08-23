


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
