# WebDriver Bidi APIs

在Selenium 4中, 引入了新的事件API, 使用户能够在事件发生时从浏览器捕获事件, 并非WebDriver用于其他API的传统请求/响应方法.

WebDriver将在内部创建针对浏览器的WebSocket连接, 用于传输事件和命令.


## 变化监测
变化监测是一种能力, 用于当特定元素的DOM发生变化时, 得以通过WebDriver BiDi捕获事件.

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
async with driver.log.mutation_events() as event:
    pages.load("dynamic.html")
    driver.find_element(By.ID, "reveal").click()
    WebDriverWait(driver, 5).until(EC.visibility_of(driver.find_element(By.ID, "revealed")))

assert event["attribute_name"] == "style"
assert event["current_value"] == ""
assert event["old_value"] == "display:none;"
```

