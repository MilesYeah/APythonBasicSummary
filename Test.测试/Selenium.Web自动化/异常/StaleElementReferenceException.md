# StaleElementReferenceException

Stale Element Reference Exception：陈旧元素引用异常

 

首先，啥情况下会出现这异常
简单来说就是，页面元素过期了，无法引用元素

 

## 出现这异常的常见原因
1. The element has been deleted entirely：该元素已被删除【更常见】
2. The element is no longer attached to the DOM：元素不再附加到DOM上
 

## 该元素已被删除
### 分析原因
造成这种情况的最常见原因：刷新了元素所在的页面，或者用户导航到另一个页面

另一个原因是：JS库删除了一个元素，并用相同的ID或属性替换了它

 

### 解决方法
再次查找该元素

 

## 元素不再附加到DOM上
### 分析原因
有可能是引导了不再附加到DOM树的元素（比如，document.documentElement）

 

### 解决方法
仍然是再次查找该元素




## 实例
```py
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document【第二种情况】
```
 
对元素hover，即调用了 Webdriver.ActionChains(driver).move_to_element(element).perform() 的方法
 
解决方法： 对异常进行捕获，并重新定位元素，重新hover

如果这样也解决不了你的问题，那么可以试试直接click元素（当然，前提是点击该元素不会触发其他任何交互，才能用click替换hover）



## ref
本文作者： 小菠萝测试笔记
本文链接： https://www.cnblogs.com/poloyy/p/12772046.html

