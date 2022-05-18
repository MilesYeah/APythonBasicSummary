# select 下拉框

radio框及checkbox框都是input元素，只是里面的type不同而已。select框 则是一个新的select标签

对于Select 选择框， Selenium 专门提供了一个 Select类 进行操作。
```py
from selenium.webdriver.support.select import Select
```
Select类 提供了如下的方法
| 方法                                             | 描述                                                   |
| ------------------------------------------------ | ------------------------------------------------------ |
|                                                  |                                                        |
| `select_by_value("v")`                           | 根据选项的 value属性值 ，选择元素。                    |
| `select_by_index(index)`                         | 根据选项的 次序 （从0开始），选择元素                  |
| `select_by_visible_text("text")`                 | 根据选项的 可见文本 ，选择元素。                       |
|                                                  |                                                        |
| 取消选项（较常用）                               |                                                        |
| `deselect_by_value("v")`                         | 根据选项的value属性值， 去除 选中元素                  |
| `deselect_by_index(index)`                       | 根据选项的次序，去除 选中元素                          |
| `deselect_by_visible_text("text")`               | 根据选项的可见文本，去除 选中元素                      |
| `deselect_all()`                                 | 去除 选中所有元素                                      |
|                                                  | 取消操作只适用于添加了multiple的下拉框，否则会报错     |
|                                                  |                                                        |
|                                                  |                                                        |
| `pro = Select(driver.find_element_by_id("pro"))` | 初始化 select 对象                                     |
| `pro.options`                                    | 返回所有选项                                           |
| `pro.all_selected_options`                       | 返回所有被选中的选项                                   |
| `pro.first_selected_option(self)`                | 选择第一个option 选项                                  |
|                                                  | 如果select没有multiple值，此时获取值为当前选择的option |
|                                                  |                                                        |
|                                                  |                                                        |


```html
<option value="foo">Bar</option>
```
就可以根据 foo 这个值选择该选项，
```py
s.select_by_value('foo')
```


```html
<option value="foo">Bar</option>
```
就可以根据 Bar 这个内容，选择该选项
```py
s.select_by_visible_text('Bar')
```






### Select单选框
对于 select单选框，操作比较简单：

不管原来选的是什么，直接用Select方法选择即可。

```py
import time

from selenium import webdriver
wd = webdriver.Chrome()
wd.get("file:///G:/Mirror/SourceCode/trials/trySelenium/t_checkbox/checkbox.html")

# 导入Select类
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element_by_id("ss_single"))

# 通过 Select 对象选中Female
select.select_by_visible_text("Female")

time.sleep(1)
wd.quit()
```





### Select多选框
对于select多选框，要选中某几个选项，要注意去掉原来已经选中的选项。例如，我们选择示例多选框中的 选项2 和 选项6
1. 可以用select类 的 deselect_all 方法，清除所有 已经选中 的选项。
2. 然后再遍历每个选项，通过 select_by_visible_text方法 选择需要的选项。



```py
import time

from selenium import webdriver
wd = webdriver.Chrome()
wd.get("file:///G:/Mirror/SourceCode/trials/trySelenium/t_checkbox/checkbox.html")

# 导入Select类
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element_by_id("ss_multi"))

# 清除所有 已经选中 的选项
select.deselect_all()

# 选择 选项2 和 选项6
select.select_by_visible_text("选项2")
select.select_by_visible_text("选项6")

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




## Select源码解读
```py
class Select(object):

    def __init__(self, webelement):
        """
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - webelement - element SELECT element to wrap

        Example:
            from selenium.webdriver.support.ui import Select \n
            Select(driver.find_element_by_tag_name("select")).select_by_index(2)
        """
```
知识点
* 实例化 Select 需要传入 select 下拉框的 webelement 
* 若传入 webelement 的 tag_name 不是 <select>..</select> 标签，则会抛出异常 UnexpectedTagNameException













# eg

## 多选

```html
<html>
<body>
    <select name="cars" multiple="multiple" size="4">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="mercedes">Mercedes</option>
        <option value="audi">Audi</option>
    </select>
</body>
</html>
```


```py
#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('file:///C:/Users/hunk/Desktop/select.html')
'''本示例中所有设置等待时间均为便于观察效果'''
time.sleep(1)
Select(driver.find_element_by_name('cars')).select_by_index(0)  #以索引选择
time.sleep(1) 
Select(driver.find_element_by_name('cars')).select_by_value('saab')  #以value属性值选择
time.sleep(1) 
Select(driver.find_element_by_name('cars')).select_by_visible_text('Mercedes') #以text 文本进行选择
time.sleep(2)
options = Select(driver.find_element_by_name('cars')).all_selected_options  #获取所有选择的option
'''这里我们遍历下看看那些值被选中'''
for option in options:
    print('已经被选中option文本值:' + option.text)
Select(driver.find_element_by_name('cars')).deselect_by_index(0)
time.sleep(1)
Select(driver.find_element_by_name('cars')).deselect_by_value('saab')  #以value属性值取消选择
time.sleep(1) 
Select(driver.find_element_by_name('cars')).deselect_by_visible_text('Mercedes') #以text 文本进行取消选择
time.sleep(1)
'''获取所有的option的text值,进行遍历通过text文本进行选择'''
Options = Select(driver.find_element_by_name('cars')).options #该方法下面会详细介绍，此处为了获取所有的options选项
for option in Options:
    Select(driver.find_element_by_name('cars')).select_by_visible_text(option.text)  #循环选择
time.sleep(1)
'''因为遍历的过程中Volvo的索引为0,Volvo则被第一个选中'''
selectOption = Select(driver.find_element_by_name('cars')).first_selected_option
print (selectOption.text)
Select(driver.find_element_by_name('cars')).deselect_all()
time.sleep(1)
driver.quit()
```












## ref

* [选择框](http://www.byhy.net/tut/auto/selenium/skills_1/)
* [python selenium-webdriver 下拉菜单处理 （九）](https://www.cnblogs.com/mengyu/p/7051260.html)
* []()
* []()
* []()
* []()
* []()




