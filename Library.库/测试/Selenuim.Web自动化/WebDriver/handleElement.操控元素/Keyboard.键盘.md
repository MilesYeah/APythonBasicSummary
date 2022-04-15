# Keyboard

Keyboard代表一个键盘事件. Keyboard操作通过使用底层接口允许我们向web浏览器提供虚拟设备输入.


## 键盘操作

selenium 提供了比较完整的键盘操作，在使用的模拟键盘操作之前需要我们导入`from selenium.webdriver.common.keys import Keys`即可，然后就可以来模拟键盘操作。


### 组合键

首先我们了解下组合键，什么是组合键，比如我们经常使用的Ctrl + A ，Ctrl + C 等都是组合键。我们先看个例子

在使用按键操作的时候我们需要借助一下send_keys()来模拟操作，Keys.CONTROL 也就是我们键盘上的Ctrl键，下面是几个常用的组合键。
```py
send_keys(Keys.CONTROL,'a') 　　#全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 　　#复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 　　#剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 　　#粘贴（Ctrl+V）
```


### 常用的键
这些常用键主要是非组合键，直接输入即可。

* 回车键 Keys.ENTER
* 删除键 Keys.BACK_SPACE
* 空格键 Keys.SPACE
* 制表键 Keys.TAB
* 回退键 Keys.ESCAPE
* 刷新键 Keys.F5


```py
class Keys(object):
    """
    Set of special keys codes.
    """

    NULL = '\ue000'
    CANCEL = '\ue001'  # ^break
    HELP = '\ue002'
    BACKSPACE = '\ue003'
    BACK_SPACE = BACKSPACE
    TAB = '\ue004'
    CLEAR = '\ue005'
    RETURN = '\ue006'
    ENTER = '\ue007'
    SHIFT = '\ue008'
    LEFT_SHIFT = SHIFT
    CONTROL = '\ue009'
    LEFT_CONTROL = CONTROL
    ALT = '\ue00a'
    LEFT_ALT = ALT
    PAUSE = '\ue00b'
    ESCAPE = '\ue00c'
    SPACE = '\ue00d'
    PAGE_UP = '\ue00e'
    PAGE_DOWN = '\ue00f'
    END = '\ue010'
    HOME = '\ue011'
    LEFT = '\ue012'
    ARROW_LEFT = LEFT
    UP = '\ue013'
    ARROW_UP = UP
    RIGHT = '\ue014'
    ARROW_RIGHT = RIGHT
    DOWN = '\ue015'
    ARROW_DOWN = DOWN
    INSERT = '\ue016'
    DELETE = '\ue017'
    SEMICOLON = '\ue018'
    EQUALS = '\ue019'

    NUMPAD0 = '\ue01a'  # number pad keys
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    MULTIPLY = '\ue024'
    ADD = '\ue025'
    SEPARATOR = '\ue026'
    SUBTRACT = '\ue027'
    DECIMAL = '\ue028'
    DIVIDE = '\ue029'

    F1 = '\ue031'  # function  keys
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'

    META = '\ue03d'
    COMMAND = '\ue03d'
```


## sendKeys
即使遇到修饰符键序列, sendKeys也会在DOM元素中键入键序列. 这里 是WebDriver能够支持的键位列表.

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

# Navigate to url
driver.get("http://www.baidu.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)
```



## key_down
keyDown用于模拟按下辅助按键(CONTROL, SHIFT, ALT)的动作.
```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.baidu.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.ID, "kw").send_keys("webdriver" + Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
```

## key_up
keyUp用于模拟辅助按键(CONTROL, SHIFT, ALT)弹起或释放的操作.

```py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.baidu.com")

# Store baidu search box WebElement
search = driver.find_element(By.ID, "kw")

action = webdriver.ActionChains(driver)

# Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action.key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()
```


## clear
清除可编辑元素的内容. 这仅适用于可编辑且可交互的元素, 否则Selenium将返回错误(无效的元素状态或元素不可交互).


```py
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.baidu.com")
# Store 'SearchInput' element
SearchInput = driver.find_element(By.ID, "kw")
SearchInput.send_keys("selenium")
# Clears the entered text
SearchInput.clear()
```




# eg
## 键盘操作
### 组合键 

```py
#-*- coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('AAAAAAAAAAAA')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')  #注意这里组合键的输入。
time.sleep(10)
driver.quit()
```


### 常用建

```py
#-*- coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://cn.bing.com/")
driver.find_element_by_id('sb_form_q').send_keys('selenium')
driver.find_element_by_id("sb_form_go").send_keys(Keys.ENTER)   #通过回车键来代替鼠标的左键
driver.quit()
```






# ref
* [ActionChains](http://www.byhy.net/tut/auto/selenium/skills_2/)
* [python selenium-webdriver 元素操作之键盘操作（五）](https://www.cnblogs.com/mengyu/p/6942584.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
