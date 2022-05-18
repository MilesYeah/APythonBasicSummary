# radio.checkbox.选择框

常见的选择框包括： radio框、checkbox框、select框


## radio框
radio框选择选项，直接用WebElement的click方法，模拟用户点击就可以了。


```py
import time

from selenium import webdriver

dr = webdriver.Chrome()
dr.get('file:///E:/Development/trials/tSelenium/tcheckbox/checkbox.html')

# 获取当前选中的元素
element = dr.find_element_by_css_selector('#s_radio input[checked=checked]')
print('当前选中的是: ' + element.get_attribute('value'))

# 点选 小雷老师
dr.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()

dr.quit()
```







## checkbox框
对checkbox进行选择，也是直接用 WebElement 的 click 方法，模拟用户点击选择。

需要注意的是，要选中checkbox的一个选项，必须 先获取当前该复选框的状态 ，如果该选项已经勾选了，就不能再点击。否则反而会取消选择。

我们的思路可以是这样：
* 先把 已经选中的选项全部点击一下，确保都是未选状态
* 再点击 小雷老师

```py
import time

from selenium import webdriver
wd = webdriver.Chrome()
wd.get("file:///G:/Mirror/SourceCode/trials/trySelenium/t_checkbox/checkbox.html")

# 先 找到所有已选中的选项框，把已经选中的选项全部点击一下
elements = wd.find_elements_by_css_selector(
  '#s_checkbox input[checked="checked"]')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element_by_css_selector(
  "#s_checkbox input[value='小雷老师']").click()

time.sleep(1)
wd.quit()
```



## checkbox.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>checkbox</title>
</head>
<body>
    <div id="s_radio">
      <input type="radio" name="teacher" value="小江老师">小江老师<br>
      <input type="radio" name="teacher" value="小雷老师">小雷老师<br>
      <input type="radio" name="teacher" value="小凯老师" checked="checked">小凯老师
    </div>
    <p>分割</p>
    <div id="s_checkbox">
      <input type="checkbox" name="teacher" value="小江老师">小江老师<br>
      <input type="checkbox" name="teacher" value="小雷老师">小雷老师<br>
      <input type="checkbox" name="teacher" value="小凯老师" checked="checked">小凯老师
    </div>
    <p>分割</p>
    <select id="ss_single">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat">Fiat</option>
        <option value="audi">Audi</option>
    </select>
    <p>分割</p>
　　<select id='ss_multi' style="width:120px;height:160px;" multiple="multiple">
　　　　<option value="1">选项1</option>
　　　　<option value="2">选项2</option>
　　　　<option value="3">选项3</option>
　　　　<option value="4">选项4</option>
　　　　<option value="5">选项5</option>
　　　　<option value="6">选项6</option>
　　　　<option value="7">选项7</option>
　　</select>
</body>
</html>
```







## ref

* [选择框](http://www.byhy.net/tut/auto/selenium/skills_1/)
* []()
* []()
* []()
* []()
* []()
* []()

