# ActionChains 鼠标操作

用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽等等。

而selenium给我们提供了一个类来处理这类事件—— `ActionChains`

在webdriver中，鼠标操作的方法封装在 ActionChains 类提供。


| Methods inherited                                           | 描述                                                           |
| ----------------------------------------------------------- | -------------------------------------------------------------- |
| `__exit__(_type, _value, _traceback)`                       |                                                                |
| `__init__(driver)`                                          |                                                                |
|                                                             |                                                                |
| 鼠标操作                                                    |                                                                |
| `click(on_element=None)`                                    | 左键点击                                                       |
| `click_and_hold(on_element=None)`                           | 长按                                                           |
| `context_click(on_element=None)`                            | 右键点击                                                       |
| `double_click(on_element=None)`                             | 双击                                                           |
| `drag_and_drop(source, target)`                             | 拖动 将源元素拖动到目标元素处                                  |
| `drag_and_drop_by_offset(source, xoffset, yoffset)`         | 拖动 将源元素拖动指定偏移量                                    |
| `key_down(value, element=None)`                             |                                                                |
| `key_up(value, element=None)`                               |                                                                |
| `move_by_offset(xoffset, yoffset)`                          | 鼠标移动到距离当前位置（x,y）                                  |
| `move_to_element(to_element)`                               | 悬停到设置按钮，鼠标移动到某个元素                             |
| `move_to_element_with_offset(to_element, xoffset, yoffset)` | 悬停到指定偏移量, 将鼠标移动到距某个元素多少距离的位置         |
|                                                             | 是先找到元素，再根据元素位置偏移指定偏移量                     |
|                                                             |                                                                |
| pause(seconds)                                              |                                                                |
| perform(self)                                               | 执行链中的所有动作, 所有的操作都需要执行 perform               |
|                                                             | 调用其他操作方法后，都要再次调用这个方法，表示执行某个鼠标操作 |
| release(on_element=None)                                    | 在某个元素位置松开鼠标左键                                     |
| reset_actions(self)                                         |                                                                |
| send_keys(*keys_to_send)                                    | 在文本框内输入内容                                             |
| send_keys_to_element(element, *keys_to_send)                |                                                                |
|                                                             |                                                                |
|                                                             |                                                                |
| 键盘操作                                                    |                                                                |
| `from selenium.webdriver.common.keys import Keys`           |                                                                |
| element.send_keys(Keys.BACK_SPACE)                          | 删除键（BackSpace）                                            |
| element.send_keys(Keys.SPACE)                               | 空格键(Space)                                                  |
| element.send_keys(Keys.TAB)                                 | 制表键(Tab)                                                    |
| element.send_keys(Keys.ESCAPE)                              | 回退键（Esc）                                                  |
| element.send_keys(Keys.ENTER)                               | 回车键（Enter）                                                |
| element.send_keys(Keys.CONTROL,'a')                         | 全选（Ctrl+A）                                                 |
| element.send_keys(Keys.CONTROL,'c')                         | 复制（Ctrl+C）                                                 |
| element.send_keys(Keys.CONTROL,'x')                         | 剪切（Ctrl+X）                                                 |
| element.send_keys(Keys.CONTROL,'v')                         | 粘贴（Ctrl+V）                                                 |
| element.send_keys(Keys.F1)                                  | 键盘   F1                                                      |
| ……                                                          |                                                                |
| element.send_keys(Keys.F12)                                 | 键盘   F12                                                     |
|                                                             |                                                                |
|                                                             |                                                                |



## 鼠标操作

我们以移动鼠标到某个元素为例。

百度首页的右上角，有个 更多产品 选项，

如果我们把鼠标放在上边，就会弹出 下面的 糯米、音乐、图片 等图标。

使用 ActionChains 来 模拟鼠标移动 操作的代码如下：

```py
from selenium import webdriver

driver = webdriver.Chrome(r'f:\chromedriver.exe')
driver.implicitly_wait(5)

driver.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)

# 鼠标移动到 元素上
ac.move_to_element(
    driver.find_element_by_css_selector('[name="tj_briicon"]')
).perform()
```






## 实例

如下实例中使用到的页面可以通过 [网址](https://files.cnblogs.com/files/mengyu/%E6%B5%8B%E8%AF%95%E6%96%87%E4%BB%B6.rar) 进行下载。

## AcitonChains

链条式方法
```py
searchElement = driver.find_element_by_id('sb_form_q').send_keys('selenium')
searchButtonElement = driver.find_element_by_id('sb_form_go')
ActionChains(driver).click(searchButtonElement).perform()     #使用一行将所有的步骤写完
```
分布式方法
```py
searchElement = driver.find_element_by_id('sb_form_q').send_keys('selenium')
searchButtonElement = driver.find_element_by_id('sb_form_go')
ActionChainsDriver = ActionChains(driver).click(searchButtonElement)   #分开两步进行书写
ActionChainsDriver.perform()
```

## 鼠标操作

### 鼠标点击 click

```py
#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/hunk/Desktop/demo_clicks.html')
driver.maximize_window()
# 首先我们需要获取到要操作的元素，然后再次进行操作
doubleButtonElement = driver.find_element_by_xpath('/html/body/form/input[2]')   #获取双击按钮元素
buttonElement = driver.find_element_by_xpath('/html/body/form/input[3]')         #获取单击按钮元素
rightButtonElement = driver.find_element_by_xpath('/html/body/form/input[4]')    #获取右击按钮元素
clickHoldElement = driver.find_element_by_xpath('/html/body/form/input[5]')      #获取按住不放按钮元素
'''内容开始的时候我们也介绍说明，当调用perform()方法时才会执行鼠标操作'''
#双击操作
ActionDoubleClick= ActionChains(driver).double_click(doubleButtonElement)
ActionDoubleClick.perform() 
time.sleep(3)
# 单击操作
ActionClick = ActionChains(driver).click(buttonElement)
ActionClick.perform()
time.sleep(3)
# 右击操作
ActionContextClick = ActionChains(driver).context_click(rightButtonElement)
ActionContextClick.perform()
time.sleep(3)
#按住不放左键
ActionClickHold = ActionChains(driver).click_and_hold(clickHoldElement)
ActionClickHold.perform()
time.sleep(3)
driver.quit()
```


### 鼠标移动 move

```py
#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/hunk/Desktop/text3.html')
driver.maximize_window()
#第一个操作:鼠标移动到某个元素
#为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
MoveElement = driver.find_element_by_xpath('//*[@id="box1"]')   #鼠标移到到目标元素
time.sleep(3)
'''将鼠标移到MoveElement'''
Action = ActionChains(driver)

Action.move_to_element(MoveElement).perform()
time.sleep(5)
driver.save_screenshot('move_to_element.png')   #记录一下我们开始的坐标位置
'''x坐标为正数向右偏移，x坐标为负数向左偏移'''
'''y坐标为正数向下偏移，y坐标为负数向上偏移'''
#为了更好的显示我们效果，当鼠标移动到目标位置的时候，我们显示了鼠标的坐标，以后让当前的位置变成绿色
Action.move_by_offset(-311,-11).perform() #move_by_offset以鼠标当前的位置为中心进行偏移，移动到距离当前位置(x,y)
time.sleep(5)
driver.save_screenshot('move_by_offset.png')   #记录一下我们移动后的坐标位置
driver.quit()
```




### 鼠标拖拽 drag

```py
#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/hunk/Desktop/text3.html')
driver.maximize_window()
#第一个操作:鼠标移动到某个元素
#为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
dragElement = driver.find_element_by_xpath('//*[@id="box1"]')   #获取被拖拽的元素
targetElement = driver.find_element_by_xpath('//*[@id="area1"]')   #获取被拖拽到的目标
Action = ActionChains(driver)
'''将【拖拽我吧！】元素拖拽到第一个对话框'''
Action.drag_and_drop(dragElement,targetElement).perform()   #将【拖拽我吧！】拖到第一个对话框
time.sleep(5)
'''将【拖拽我吧！】元素拖拽到距离当前位置(45,200)，也就是拖拽到第二个对话框'''
'''由于第一次我们已经将元素拖拽到了第一个对话框，所以我们实际的拖拽是从第一个对话框拖拽到第二个对话框'''
Action.drag_and_drop_by_offset(dragElement,45,200).perform()
time.sleep(5)
driver.quit()
```


上面讲解的拖拽是selenium自己带的拖拽方法，我们是否可以讲鼠标的移动和点击生成一个新的拖拽

首先我们来思考一下如何实现拖拽？

我们需要选择一个元素然后按住鼠标左键到某个地方松开鼠标实现拖拽
```py
#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get('file:///C:/Users/hunk/Desktop/text3.html')
driver.maximize_window()
#第一个操作:鼠标移动到某个元素
#为了演示，开始设置标签的颜色淡蓝色，当鼠标移到到该元素时标签颜色变为红色
dragElement = driver.find_element_by_xpath('//*[@id="box1"]')   #获取被拖拽的元素
targetElement = driver.find_element_by_xpath('//*[@id="area3"]')   #获取被拖拽到的目标
Action = ActionChains(driver)
'''将【拖拽我吧！】元素拖拽到第三个对话框'''
#首先选择元素，按住不放，然后移动元素，最后松开鼠标，完成拖拽
Action.click_and_hold(dragElement).move_to_element(targetElement).release().perform()
time.sleep(5)
driver.quit()
```


# ref
* [ActionChains](http://www.byhy.net/tut/auto/selenium/skills_2/)
* [python selenium-webdriver 元素操作之鼠标操作（四）](https://www.cnblogs.com/mengyu/p/6901489.html)
* [python selenium-webdriver 元素操作之键盘操作（五）](https://www.cnblogs.com/mengyu/p/6942584.html)
* [python和selenium实现Web自动化(2)：鼠标操作和键盘操作！](https://blog.csdn.net/weixin_48500307/article/details/108450699)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
