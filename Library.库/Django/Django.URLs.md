# Django URLs



## URL congigurations

包含其他URL
* 在url.py中引入include
* 在APP目录下创建urls.py，格式与跟urls.py相同
* 将urls.py中url函数第二个参数改为include('blog.urls')

* 注意事项
  * 跟urls.py针对APP配置的URL名称是该APP所有URL的总路径
  * 配置URL时注意正则表达式结尾符号$和/



## url传递参数
* 参数写在响应函数request之后，可以有默认值
* URL正则表达式：r'^/article/(?P<article_id>\d+)/$'
* URL正则中的组名必须和参数名一致


## 超链接目标地址
* href后面是目标地址
* template中可以用 \{\% url 'app_name:url_name' param \%\} 
* 其中app_name和url_name都在url中配置


## URL函数的名称参数
* 跟urls，写在include()的第二个参数位置，namespace='app_name'
* 应用下则写在url()的第三个参数位置，name='url_name'
* 在应用的urls.py文件中，加入参数 app_name = 'app_name'


## URL先后顺序
* 在编写urlpatterns的时候，使用正则表达式时，养好习惯加上匹配行首`^`行尾`$`。
  * 否则如果类似的正则表达式出现的时候，Django有可能会使用一个不正确的url。
  * 如`url(r'form/$', getform)`和`url(r'formadmin/', admin)`，
  * 实际上在访问formadmin的时候，实际访问的是form页面。
  * 解决办法是加入行尾匹配符：`url(r'form/$', getform)`和`url(r'formadmin/', admin)`

