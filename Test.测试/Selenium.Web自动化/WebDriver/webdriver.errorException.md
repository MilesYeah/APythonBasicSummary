

## 调试自己的自动化脚本代码的时候：
1. 仔细地去观察脚本执行过程中浏览器的操作。
2. 常见异常的处理方法：仔细阅读报错异常信息。

### session not created 浏览器和webdriver版本不配套。
	1、session not created: This version of ChromeDriver only supports Chrome version 83
		chrome版本更新了，webdriver不配套。
		环境变量如果配置完了，记得重启使用环境变量的应用，比如IDEA	


### Invalid Argument: 非法参数。  
可能原因：
1. 用户目录被占用的情况下，启动了带用户目录的浏览器。
2. get方法请求网址的时候，没有带上协议http://


## no such element: 没有这个元素。
`no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="auto-id-Q5zyQNpTsLMmUVHX"]/a"}`
可能原因：
1. 元素定位表达式错误：	
    1. 先确认当前浏览器中，表达式是能够定位到元素的。	
    2. 确认表达式中是否包含了随机生成的字段。
2. 如果浏览器操作过程中打开了新的窗口，要在代码中进行切换，否则webdriver的操作方式是接着在之前的页面中进行操作。
   1. selenium会给打开的新窗口编个号，产生一个唯一的句柄来标识每个窗口。
3. 元素有可能在iframe（内联框架，类似于画中画）中。
4. 如果出现偶现的定位失败，有可能是因为网页加载速度的问题，可以通过等待浏览器加载来解决。
   1. 针对于元素定位：通用方法添加隐式等待。 当进行元素定位的时候，有10秒的机会。
   2. 注意：隐式等待只需要设置一次，建议在脚本开头固定添加。
   3. 页面加载太慢导致findelement以外的方法执行不了： 可以考虑添加固定等待。
   4. 线程休眠thread.sleep()



### element click intercepted：元素不支持点击操作（element not interactable 元素无法互动）
`Exception in thread "main" org.openqa.selenium.ElementNotInteractableException: element not interactable   元素无法互动，不能响应。`

`element click intercepted: Element <i>...</i> is not clickable at point (663, 510). Other element would receive the click: <a href="javascript:;" class="u-btn2 u-btn2-2 u-btn2-w2 j-flag" hidefocus="true" id="auto-id-4KoII1VaUWL0OSC0">...</a>`

排查步骤：
1. 可以根据提示，直接用提示的元素来进行操作。  
2. 先确认在开发者工具中元素定位表达式正确
   1. 可能是找错了元素，比如要去点击一个超链接a，定位的是一个em span等等。
   2. elements中按下ctrl+f，逐步验证表达式正确性。
   3. 调用验证过的js脚本：
      1. document.querySelector('[href="/friend"]').click()
      2. 基于css选择器的dom语法定位元素并且操作，可以在selenium脚本中通过js执行器进行调用。
   4. 手写xpath：
        //*[contains(@id,'auto-id')]
        //开头，表示在整个网页html中搜索符合条件的元素。
        //在表达式中间，表示基于前面的元素找子孙元素。

        /在表达式中间，表示基于前面的元素找直接子元素。
        
        //元素名  *号表示任意元素。
        [限制条件表达式]  表示元素需要满足的条件
        @属性 =‘value’  表示元素的属性值需要等于value
        text()或者string()=‘value’ 表示元素的文字内容等于value
        contains（@属性，'value'）  表示元素的属性值包含value。
   5. css 
       1. [href='/friend']   表示定位任意的一个元素，href属性是/friend
3. 通过开发者工具验证一下是否能够通过js来进行元素的调用。
   1. $x("//a[text()='登录']")[0].click()   
   2. console控制台中，通过$x("xpath")[0]表达式获取元素进行简单的调试，至少确认元素能够通过js来进行调用。
   3. 即使selenium无法调用，还可以通过js来执行。
   4. 建议少用js，更多去模拟用户真实操作。
4. 检查是不是弄错了操作的元素。 基于对于html元素的理解。
5. 确认浏览器的范围，最好最大化。
6. 是否需要时间等待这个元素的加载完成。最好的办法：加个隐式等待。
7. 可以在浏览器console控制台里面进行代码调试，如果可用，再写到代码里面。
8. 有些元素在html中只是用来表示这个内容用斜体显示，没有其它功能，
   1. 比如 **<li>**
   2. 如果前端没有用js去实现对它的操作响应，点击就有可能无效。

### element not interactable： 元素无法被操作。
可能是元素没有在浏览器显示的范围之内
解决方案： 把浏览器最大化再执行。



### 在web自动化过程中要注意的
1. 浏览器和webdriver使用配套版本。
2. 注意get里面url带http
3. 如果要使用浏览器用户配置文件，那么最好是单独复制一份进行使用，或者在自动化测试执行的时候关闭已经手动打开的浏览器。
4. 定位元素的时候：
    1. 如果编写定位表达式，先在浏览器中确认表达式正确性。并且确认其中没有随机变化的字段。
5. 窗口进行切换
    1. 先在代码中加个隐式等待，至少避免多数情况下的元素定位不到需要等待加载的问题。 提前预防。
       1. driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
    2. 如果还报错，检查一下是否有iframe以及是否需要加等待时间，等待页面完成加载。
    3. 碰到新窗口进行切换（注意，回到旧窗口也要切换。）
6. 确认检查某些看起来就不对的元素是否能进行操作，用js可以先验证一下。









## NoSuchElementException：
1. 添加隐式等待（显示等待）
2. 添加固定等待
3. 确保你的定位是稳定的切调试通过的
4. iframe切换
5. 切换窗口


