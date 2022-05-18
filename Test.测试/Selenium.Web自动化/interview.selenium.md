# Selenium 面试宝典

## 为什么选择 Selenium 做自动化？
* 免费、开源
* 有庞大的用户群体和社区，随时能找到难点解决办法
* 跨浏览器兼容性：Chrome、Firefox、IE、Safari
* 平台兼容性：Window、MAC、Linux
* 支持分布式测试





## Selenium 的局限性？
* 仅支持 Web 应用程序测试
* 需要结合第三方测试报告框架生成测试报告





## 定位元素的方式有几种？是什么？
8种
* id
* class
* name
* tag 标签
* css 选择器
* xpath 选择器
* 超链接文本（精确匹配）
* 超链接文本（模糊匹配）





## 如何决定选择用哪种定位表达式？
* 如果元素有 id 会优先用 id 选择器
* 如果没有 id，但有 name 属性，就会选择 name 选择器
* 其他情况一般都会用 css 选择器，因为对 css 比较熟悉
* 而且 html 本身就与 css 配合使用，所以 css 的可用性会更好
* 如果 css 选择器定位失败，会尝试 xpath 选择器，因为它也是万能选择器





## Xpath 中绝对路径和相对路径有什么优缺点？
### 绝对路径
* 优点：有层级，结构清晰，只要层级没写错肯定能找到元素
* 缺点：如果层级过深会导致表达式很长，可读性和后期维护性也不好，并且如果中间层级的元素发生了增加或减少，你的绝对 xpath 表达式就要改动，维护成本也会很高


### 相对路径
* 优点：解决了绝对路径的缺点问题，不受所有父级元素变动的影响，专注于定位需要的元素即可，表达式简洁且有效
* 缺点：需要对 xpath 语法比较熟悉才能快速写出准确而且简洁的相对 xpath 表达式，需要一定的学习成本





## css 选择器和 Xpath 选择器用哪个多点？为什么？
css 选择器
* css 的语法更简洁，能满足大部分的使用场景
* css 也是 Web 页面的组成部分，浏览器识别它的速度理论上会更快，性能会比 xpath 好很多
* css 的实现原理是匹配对象的原理，它是从右往左找元素，找元素的时候能尽量少的进行查找操作，而 xpath 的实现原理是遍历，需要从左往右找，所以查找操作更耗时
* xpath 引擎在每个浏览器中是不同的，像 IE 没有原生 xpath 引擎，所以 selenium 为了兼容性会注入自己的 xpath 引擎，这样就会失去使用 WebDriver 本地浏览器特性的优势
* 前端开发用的就是 css，技术上遇到问题可以得到开发的帮助





## 如何去定位页面上动态加载的元素？
触发动态加载元素的事件，直至动态元素出现，进行定位





## 如何去定位属性动态变化的元素？
* 如果有固定前缀、后缀值，可以通过 xpath 的模糊匹配方法，比如 `//*[contains(@id, "id")]， //*[starts-with(@class,"class")]，//*[ends-with(@name,"name")]` 
* 属性值完全随机的话，可以通过 xpath、css 选择器找到它的父级、子级、同级元素，再进行定位
* 注意：css 不能找到父级元素

| 元素 | xpath                   | css        |
| ---- | ----------------------- | ---------- |
| 父级 | //div/../span           | 无         |
| 子级 | //div/span              | div > span |
| 同级 | //div/following-sibling | div + span |







## 点击链接以后，selenium是否会自动等待该页面加载完毕？
会的，但也有一个命令超时时间





## 如何模拟鼠标操作？提供了哪些操作？
webdriver 提供了一个类：ActionChains
* 左键单击、双击
* 右键单击、双击
* 鼠标悬停（hover）
* 长按
* 拖动





## 如何 hover 元素？
* 通过导入 ﻿from selenium.webdriver import ActionChains﻿
* 然后调用 move_to_element 方法，将鼠标悬停到某个元素上





## 如何模拟键盘操作？
Webdriver 提供了个 Keys 类 `from selenium.webdriver.common.keys import Keys `





## 常见的时间等待有哪几种？
*  time.sleep() 强制等待，一般只用于调试
*  driver.implicitly_wait(20) 隐性等待，WebDriver 生命周期内都生效，一般用于页面等待
*  WebDriverWait 显性等待，只针对某个元素生效，根据需要定位的元素进行显性等待，效率会高很多





## 显性等待如何导入？它包含了哪些方法

```py
from selenium.webdriver.support.wait import WebDriverWait
```

until 和 until_not





## Selenium 提供了一个条件判断类，是什么？如何导入？

```py
from selenium.webdriver.support import expected_conditions
```






## 如何判断元素是否存在 DOM 树？
思路：元素只要出现在 DOM 树就行，不一定要可见

### 方式一：find_element + try-except
* 直接使用最简单的 find_element 获取元素，结合 try-except 捕获异常
* 因为找不到元素肯定会报错，报错就知道元素不存在了

```py
def find_element_by_try_except(locator):
    try:
        driver.find_element(*locator)
        return True
    except Exception as msg:
        print("元素%s找不到：%s" % (locator, msg))
        return False
```



### 方式二：find_elements
使用 find_elements 方法获取元素，返回是一个数组，若数组长度<1，则判断元素不存在

```py
def find_element_by_try_except(locator):
    eles = driver.find_elements(*locator)
    if len(eles) < 1:
        return False
    else:
        return True
```



### 方式三：WebDriverWait + expected_conditions
* 导入 expected_conditions 类
* 然后调用 presence_of_element_located 方法结合 WebDriverWait 定位元素
* 若返回 False 则不存在，返回 WebElement 元素则存在

```py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


element = WebDriverWait(driver, 30, 1).until(
　　EC.presence_of_element_located(locator)
)
```






## 如何判断元素是可见的？

### 方式一：is_displayed()
最简单的方法

```py
ele = driver.find_element_by_id("username")
print(ele.is_displayed())
```



### 方式二：WebDriverWait + expected_conditions
* 导入 expected_conditions 类
* 然后调用 visibility_of_element_located 方法结合 WebDriverWait 定位元素
* 若返回 False 则不可见，返回 WebElement 元素则可见

```py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
element = WebDriverWait(driver, 30, 1).until(
　　EC.visibility_of_element_located(locator))
```






## hidden 或者是 display=none 的元素是否可以定位到？能否操作？
能，但是不能操作





## 如何操作隐藏的元素？
回答顺序
* 大部分情况下，操作隐藏的元素是没有意义的
* 因为 UI 自动化是为了模拟用户正常的操作行为，用户是没办法操作隐藏元素的
* 但如果一定要操作隐藏的元素，可以通过 js 进行操作

```py
js = 'document.getElementById("username").click()' driver.execute_script(js)
```






## Selenium 提供了一个类操作下拉框，是什么？如何导入？

```py
from selenium.webdriver.support.select import Select
```






## 如何使用操作下拉框类选中下拉选项

```py
# 分两步
# 1、找到select标签元素

sel = Select(driver.find_element_by_id("select"))


# 2、可以根据 value属性、index、标签文本选中
# 通过value选中
pro.select_by_value("bj")


# 通过index选中
pro.select_by_index(1)



# 通过标签文本选中
pro.select_by_visible_text("广东")
```



### 取消选中呢？

```py
# 根据value取消选中
city.deselect_by_value("bj")
```



### 取消选中操作可以对单选框生效吗？
不能，会报错，只能对多选框生效





## 如何切换 iframe 元素？如何从 iframe 切换回主页面？

```py
# 切换至iframe
driver.switch_to.frame(iframe1)

# 切换回主页面
driver.switch_to.default_content()
```






## 如何切换到 alert 警告弹窗

```py
# 切换至对话框
alert2_ = driver.switch_to.alert


# 获取窗口值
print(alert2_.text)


# 点击 取消
alert2_.dismiss()


# 点击 确认
alert2_.accept()
```






## 如何切换浏览器标签页

```py
# 获取当前标签页句柄
driver.current_window_handle


# 获取浏览器所有标签页句柄
handles = driver.window_handles


# 切换标签页句柄
driver.switch_to.window(handles[-1])
```






## 如何进行上传文件？

### 情况一：如果是 input 标签
直接调用 send_keys 上传文件即可


```py
# 定位上传文件元素 input[type=file]
ele = driver.find_element_by_id("pic")


# 上传文件
ele .send_keys(r"C:/上传文件.html")
```



### 情况二：非 input 标签
找到上传文件的元素，然后需要调用 win32 库进行操作





## Selenium 常见的异常
* WebDriverException：浏览器版本和浏览器驱动版本不一致
* TimeoutException：命令超时，在一定时间内没有完成
* NoSuchElementException：找不到元素
* NoSuchFrameException：切换到不存在的 iframe 窗口时报错
* ElementNotVisibleException：元素存在，但不可见，操作该元素则会报错





## driver.quit()和driver.close() 的区别？
同时打开多个页面时， .close() 仅关闭当前用户正在操作的页面，而 .quit() 会关闭整个浏览器，直接退出





## 一个元素明明定位到了，点击无效（也没报错），如果解决？
使用 js 点击，selenium 有时候点击元素是会失效

```py
// 获取元素进行点击
js = 'document.getElementById("baidu").click()'


// 执行 js
driver.execute_script(js)
```






## Selenium 家族有什么工具
* Selenium IDE：浏览器组件，提供录制回放功能，可以将录制生成的脚本转换为多种编程语言的脚本
* Selenium RC（Remote Control）：一个服务端，可以处理测试脚本发送过来的HTTP请求，来操作浏览器
* Selenium Grid：支持分布式测试，可以在不同平台、不同浏览器的多台远程机器上同时运行Selenium测试脚本
* Selenium WebDriver：通过调用WebDriver对象的方法来操作浏览器





## Selenium Grid 是什么？有什么好处？
Selenium Grid 可用于在多个平台和浏览器上同时执行相同或不同的测试脚本，从而实现分布式测试执行，在不同环境下进行测试并节省执行时间





## Webdriver 的工作原理
* Selenium WebDriver 是调用浏览器的原生接口来操作浏览器的
* 测试脚本操作浏览器的过程就是在测试脚本中创建 WebDriver 对象
* 再通过这个对象调用 WebDriver API 来访问浏览器接口，从而操作浏览器的过程





## WebDriver 的实现原理
* 在测试脚本中使用 Selenium WebDriver，无论是哪个平台、哪个浏览器，处理逻辑都是通过一个 HttpComandExecutor 类发送命令，实际上就是一条发送给 WebService 的 HTTP 请求
* WebService 是基于特定 WebDriver Wire 协议的 RESTful 接口
* 测试脚本通知浏览器要做的操作存放到发送到 WebService 的 HTTP 请求体中
* 整个过程类似一个 webservice，使用 The WebDriver Wire Protocol 协议做传输



```flow
请求会调用
尚创小
HTTPCommandExecutor
client(测试本)
小泥专测试笔记
动作1
启动浏览器
步聚2:通过http发送RESTful请求
梦测试笔记
如findelement,包含浏览器操作
驱动
步豪1:通过Driver.exe驱
动作2
定位元素
测试笔记
步骤3:返回步骤2的请求响应
动作3
记
remoteserver
操作元素
创建Session,绑定ip:port
试笔记
```





## WebDriver 的副作用
不同的浏览器厂商，因为对 Web 元素操作方式有差异，所以不同的浏览器需要有不同的驱动，比如 ChromeDriver、FirefoxDriver





## WebDriver 用的协议是？
The WebDriver Wire Protocol





## 如何提高脚本的执行速度？

### 从环境层面
* 使用配置更高的硬件
* 配置独立的网络、测试专用环境拿来跑自动化测试，避免人为干扰


### 从脚本层面
* 尽量使用 css 选择器进行定位元素
* 尽量不用强制等待、隐式等待，用显式等待取代
* 可以使用 Selenium Grid 进行分布式测试，也可以结合 Pytest-dist 进行分布式测试





## 如何去提升用例、脚本的稳定性？
用例在运行过程中经常会出现不稳定的情况，也就是说这次可以通过，下次就没办法通过了

### 前置回答，告诉面试官你理解的稳定性好是怎么样的
* 两方面：长时间的稳定性、频繁运行的稳定性
* 在项目不断更新迭代的过程中，需要进行 UI 回归自动化测试时，旧用例都能跑成功，不会出现项目每迭代一次，用例/脚本就会跑失败的情况
* 用例在一段时间内不断重复运行，用例全部都跑成功，不会出现大部分成功而几次失败的情况


### 从环境层面
* 保证网络的顺畅性
* 保证项目的可用性


### 从代码层面
* 减少用例之间的依赖，保证所有用例都能无序运行、单独运行
* 从框架层面，添加失败重试机制，比如 Pytest 的 rerun 插件，自定义重试次数和频率
* 从项目层面，添加错误截图的方法，利用 Pytest 的 hook 自定义错误截图的方法，全局生效，方便在报错时及时了解页面的具体展示情况
* 从代码层面，给封装的方法（比如定位元素、操作元素、操作文件等方法）添加异常捕获机制，若捕获到指定异常则再次运行一次代码或换个方法再次执行
* 通过显式等待 + expect_conditions 类的方法封装常用方法，如：定位元素，点击，输入文本，判断元素是否可选中点击、选中元素等，提高方法复用性的同时也提高了健壮性
* 对于封装的操作元素方法内部，在操作元素前，先判断元素是否可见，若可见再进行操作





## 如何保证操作元素的成功率？
也就是说如何保证我点击的元素一定是可以点击的
* 通过显式等待 + expect_conditions 类的方法封装点击方法
* 点击前先判断元素是否可点击
* 捕获指定异常后（比如：ElementClickInterceptedException），可以重新定位元素后再次点击





## 你的自动化用例的执行策略是什么？
* 定时执行，可以结合 Jenkins 的定时任务达到目的
* 将主流程需要回归测试的用例通过 Jenkins 构建触发器绑定开发的 Git 仓库，当开发在灰发环境提交代码后自动运行这部分的用例
* 其他优先级不算特别高的用例可以一周定时执行一次





## 有没有考虑过约束前端开发的一些元素属性规则，然后利于我们开展自动化？怎么约束？
有做过一些比较简单的约束吧，也是在他们原有的基础上改进的
* 编码统一为 utf-8
* id 必须是唯一的，且仅用在大的模块上
* 大模块下的子元素用 class 命名，开头用父类 id 名，后面接下划线 _ 然后接子类英文缩写，不使用拼音，有从属命名的关系
* id 和 class 不允许重名
* 如果有 input 标签，需要有一个唯一的名字，除非功能相同




















## ref
* [Selenium 面试宝典](https://www.yuque.com/poloyy/xgkn5u/yfgwfb)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

