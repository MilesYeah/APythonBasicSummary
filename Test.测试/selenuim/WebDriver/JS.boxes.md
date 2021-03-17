# JS.boxes

WebDriver提供了一个API, 用于处理JavaScript提供的三种类型的原生弹窗消息. 这些弹窗由浏览器提供限定的样式.


## Alerts 警告框
其中最基本的称为警告框, 它显示一条自定义消息, 以及一个用于关闭该警告的按钮, 在大多数浏览器中标记为"确定”(OK). 在大多数浏览器中, 也可以通过按"关闭”(close)按钮将其关闭, 但这始终与“确定”按钮具有相同的作用. 查看样例警告框.

WebDriver可以从弹窗获取文本并接受或关闭这些警告.


```py
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See an example alert").click()

# Wait for the alert to be displayed and store it in a variable
alert = wait.until(expected_conditions.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()
```


## Confirm 确认框
确认框类似于警告框, 不同之处在于用户还可以选择取消消息. 查看样例确认框.

此示例还呈现了警告的另一种实现:

```py
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample confirm").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = driver.switch_to.alert

# Store the alert text in a variable
text = alert.text

# Press the Cancel button
alert.dismiss()
```



## Prompt 提示框
提示框与确认框相似, 不同之处在于它们还包括文本输入. 与处理表单元素类似, 您可以使用WebDriver的sendKeys来填写响应. 这将完全替换占位符文本. 按下取消按钮将不会提交任何文本. 查看样例提示框.


```py
# Click the link to activate the alert
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# Wait for the alert to be displayed
wait.until(expected_conditions.alert_is_present())

# Store the alert in a variable for reuse
alert = Alert(driver)

# Type your message
alert.send_keys("Selenium")

# Press the OK button
alert.accept()
```

