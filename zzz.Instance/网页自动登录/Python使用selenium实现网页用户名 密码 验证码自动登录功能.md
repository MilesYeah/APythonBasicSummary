[Python使用selenium实现网页用户名 密码 验证码自动登录功能](https://www.jb51.net/article/140239.htm)


 更新时间：2018年05月16日 10:16:26   作者：clarkxhb   我要评论
这篇文章主要介绍了Python使用selenium实现网页用户名 密码 验证码自动登录功能，实现思路很简单，感兴趣的朋友跟随脚本之家小编一起学习吧

好久没有学python了，反正各种理由吧（懒惰总会有千千万万的理由），最近网上学习了一下selenium，实现了一个简单的自动登录网页，具体如下。

1.安装selenium：

如果你已经安装好anaconda3,直接在windows的dos窗口输入命令安装selenium：

python -m pip install --upgrade pip

查看版本pip show selenium

2.接着去http://chromedriver.storage.googleapis.com/index.html下载chromedriver.exe（根据chrome的版本下载对应的）

3.将下载好的chromedriver.exe解压后放到指定目录

4.安装tesseract-ocr.exe 配置环境变量

5.安装pytesseract : pip install pytesseract

6.python脚本

思路：6.1登录页面按F12检查元素，获取用户名 密码 验证码 验证码图片的元素id

　　　6.2.调用chromedriver

　　　6.3.截取验证码图片的位置

　　　6.4.pytesseract识别图片中字符，最后验证码识别为空！！？？？这个待解决

　　　6.5.脚本如下：

```py
from selenium import webdriver
from PIL import Image
import pytesseract
import os,time
chromedriver = "D:\Program Files\Anaconda3\selenium\webdriver\chromedriver.exe" #这里写本地的chromedriver 的所在路径
os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
driver = webdriver.Chrome(chromedriver)
driver.get("http://xxxx.com") #该处为具体网址
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化
#获取全屏图片，并截取验证码图片的位置
driver.get_screenshot_as_file('a.png')
location = driver.find_element_by_id('imgValidateCode').location
size = driver.find_element_by_id('imgValidateCode').size
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.png")
im = a.crop((left,top,right,bottom))
im.save('a.png')
time.sleep(1)
#打开保存的验证码图片
image = Image.open("a.png")
#图片转换成字符
vcode = pytesseract.image_to_string(image)
print(vcode)
#填充用户名 密码 验证码
driver.find_element_by_id("staffCode").send_keys("username")
driver.find_element_by_id("pwd").send_keys("password")
driver.find_element_by_id("validateCode").send_keys(vcode)
#点击登录 
driver.find_element_by_id("loginBtn").click()
```
