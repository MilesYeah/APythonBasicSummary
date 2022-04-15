# selenium常见异常类

## 最常见异常类
### 异常：selenium.common.exceptions.WebDriverException(msg=None, screen=None, stacktrace=None)

1. 基类：exceptions.Exception
2. 描述：WebDriver基础的异常类

 

### 异常：selenium.common.exceptions.TimeoutException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：一条命令在足够的时间内没有完成则会抛出异常

 

### 异常：selenium.common.exceptions.StaleElementReferenceException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：一个参考的元素现在是“过时”时抛出异常，“过时”是指这个元素不再出现在页面的Dom中。

 

### 异常：selenium.common.exceptions.NoSuchElementException(msg=None, screen=None, stacktrace=None)

1. 基类:selenium.common.exceptions.WebDriverException
1. 描述：元素不能被找到时异常抛出

 

### 异常：selenium.common.exceptions.NoSuchAttributeException(msg=None, screen=None, stacktrace=None)

1. 基类：selenium.common.exceptions.WebDriverException
1. 描述：当元素的属性不能被发现时异常抛出

 

### 异常：selenium.common.exceptions.NoAlertPresentException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：切换到没有弹出的alert弹窗时抛出异常

 

### 异常：selenium.common.exceptions.NoSuchFrameException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.InvalidSwitchToTargetException
1. 描述：切换进不存在的iframe窗口时抛出异常

 

### 异常：selenium.common.exceptions.InvalidElementStateException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：无效的元素状态

 

### 异常： selenium.common.exceptions.ElementNotSelectableException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.InvalidElementStateException
1. 描述：当尝试选择一个不能被选中的元素时，异常会抛出

 

### 异常：selenium.common.exceptions.ElementNotVisibleException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.InvalidElementStateException
1. 描述：元素在DOM树中，但它是不可见的（display:none），操作该元素，异常将抛出

 

## 不常见的异常类
### 异常：selenium.common.exceptions.ErrorInResponseException(response, msg)

1. 基类:selenium.common.exceptions.WebDriverException
1. 描述：服务器端有错误时，异常将抛出（这个原因可能是因为Firefox插件或者远程server）

 

### 异常：selenium.common.exceptions.ImeActivationFailedException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：激活输入法失败时异常会抛出。

 

### 异常：selenium.common.exceptions.ImeNotAvailableException(msg=None, screen=None, stacktrace=None)

1. 基类:selenium.common.exceptions.WebDriverException
1. 描述：当输入法不支持的时候异常将抛出。

 

### 异常：selenium.common.exceptions.InvalidCookieDomainException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：试图在不同的domain而不是目前的URL中添加一个cookie时抛出异常

 

### 异常：selenium.common.exceptions.InvalidSelectorException(msg=None, screen=None, stacktrace=None)

1. 基类:selenium.common.exceptions.NoSuchElementException
1. 描述：当选择器没有返回一个web元素时，异常抛出。

 

### 异常：selenium.common.exceptions.InvalidSwitchToTargetException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述： 当切换的窗口或者框架不存在的时候，异常将抛出。

 

### 异常：selenium.common.exceptions.MoveTargetOutOfBoundsException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：提供给ActionChainsmovable()方法的目标无效时，异常将抛出，例如：超出文件外

 

### 异常：selenium.common.exceptions.NoSuchWindowException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.InvalidSwitchToTargetException
1. 描述：需要切换的目标窗口不存在时，异常抛出

 

### 异常：selenium.common.exceptions.RemoteDriverServerException(msg=None, screen=None, stacktrace=None)

1. 基类：selenium.common.exceptions.WebDriverException
1.  

### 异常：selenium.common.exceptions.UnableToSetCookieException(msg=None, screen=None, stacktrace=None)

1. 基类： selenium.common.exceptions.WebDriverException
1. 描述：当一个驱动程序无法设置cookie时抛出异常。

 

### 异常：　selenium.common.exceptions.UnexpectedAlertPresentException(msg=None, screen=None, stacktrace=None)

1. 基类：　selenium.common.exceptions.WebDriverException
1. 描述：当一个意外的警告出现时将抛出异常。

 

### 异常：　selenium.common.exceptions.UnexpectedTagNameException(msg=None, screen=None, stacktrace=None)

1. 基类：　selenium.common.exceptions.WebDriverException
1. 描述：辅助类没有获取到期待的web元素时，会抛出异常



## ref
本文作者： 小菠萝测试笔记
本文链接： https://www.cnblogs.com/poloyy/p/12769425.html

