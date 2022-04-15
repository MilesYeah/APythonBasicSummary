# EC expected_conditions

expected_conditions 是selenium中的一个模块，包含一系列用于判断的条件类，一共26个类


## presence_of_element_located
检查当前DOM树种是否存在该元素（和是否可见没有关系），只要有一个元素加载出来则通过

```py
class presence_of_element_located(object):
    """ An expectation for checking that an element is present on the DOM
    of a page. This does not necessarily mean that the element is visible.
    locator - used to find the element
    returns the WebElement once it is located
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return _find_element(driver, self.locator)
```

### locator参数 
传入一个元组，格式如下 （By.ID, "元素ID"） 
* 第一个参数：定位元素的方式，和那八种元素定位方式一样，只是这里需要引入 By 模块，然后再调用类属性 
* 第二个参数：和之前调用元素定位方法一样传参即可 
* 所以正确写法是： `presence_of_element_located((By.ID, "kw"))`



## presence_of_all_elements_located

```py
class presence_of_all_elements_located(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return _find_elements(driver, self.locator)
```

唯一要注意的点就是 
* 因为调用的是 _find_elements ，会返回多个元素
* 如果用这个条件类，必须等所有匹配到的元素都加载出来才通过






## 实例

```py
# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020/3/25 17:52
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# 加载驱动
driver = webdriver.Chrome()


def wait_element(driver, by_, element_, timeout=10):
    element = WebDriverWait(driver, timeout=timeout).until(
        ec.presence_of_element_located(
            (by_, element_)
        )
    )
    return element


def wait_elements(driver, by_, element_, timeout=10):
    element = WebDriverWait(driver, timeout=timeout).until(
        ec.presence_of_all_elements_located(
            (by_, element_)
        )
    )
    return element


# 加载驱动
driver = webdriver.Chrome()

# 打开网站
driver.get("http://www.51job.com")
driver.maximize_window()

# 高级搜索
more_btn = wait_element(driver, By.CLASS_NAME, "more").click()

# 职位框
wait_element(driver, By.ID, "kwdselectid").send_keys("python")

# 城市按钮
driver.find_element_by_id("work_position_click").click()

# layer
layer = wait_element(driver, By.ID, "work_position_layer")
# 城市列表
city_list = wait_elements(driver, By.CSS_SELECTOR, "div#work_position_click_center_right_list_000000 table em.on")
for city in city_list:
    sleep(1)
    city.click()

# 杭州
wait_element(driver, By.ID, "work_position_click_center_right_list_category_000000_080200").click()

# 确认
wait_element(driver, By.ID, "work_position_click_bottom_save").click()

# form
wait_element(driver, By.CSS_SELECTOR, "div#historylist>div.r1").click()

# 职能类别
wait_element(driver, By.ID, "funtype_click").click()

# 职能弹窗
type_layer = wait_element(driver, By.ID, "funtype_layer")

# 后端开发
wait_element(driver, By.ID, "funtype_click_center_right_list_category_0100_0100").click()

# f如果有已选列表，取消选择
flag = wait_element(driver, By.ID, "funtype_click_multiple_selected")
if flag.text:
    # 已选列表
    type_list = wait_elements(driver, By.CSS_SELECTOR, "div#funtype_click_multiple_selected>span")
    for types in type_list:
        if types.text == "高级软件工程师":
            continue
        em = types.find_element_by_tag_name("em")
        em.click()

# 高级软件工程师
wait_element(driver, By.ID, "funtype_click_center_right_list_sub_category_each_0100_0106").click()

# 确定
driver.find_element_by_id("funtype_click_bottom_save").click()

# 公司性质
company = wait_element(driver, By.ID, "cottype_list")
company.click()

# 列表
ctype_list = company.find_elements_by_css_selector("div.ul > span")
for ctype in ctype_list:
    # 外资（欧美）没有数据
    if ctype.text == "上市公司":
        ctype.click()
        break

# 工作年限
workyear_list = wait_element(driver, By.ID, "workyear_list")
workyear_list.click()

# 列表
wlist = workyear_list.find_elements_by_css_selector("div.ul > span")
for wtype in wlist:
    if wtype.text == "1-3年":
        wtype.click()
        break

# 搜索按钮
wait_element(driver, By.CSS_SELECTOR, "div.btnbox > span.p_but").click()

# 职位列表
resultList = wait_elements(driver, By.CSS_SELECTOR, "div#resultList>div.el")[1:]
for res in resultList:
    spans = res.find_elements_by_tag_name("span")
    texts = [x.text for x in spans]
    # 最终输出
    print(" | ".join(texts))

sleep(10)
driver.quit()
```



