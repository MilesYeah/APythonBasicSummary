# Django URLs

* [URL调度器](https://docs.djangoproject.com/zh-hans/3.1/topics/http/urls/)

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
* URL正则表达式：`r'^/article/(?P<article_id>\d+)/$'`
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
  * 否则如果类似的正则表达式出现的时候，Django有可能会使用一个不正确的url。如`url(r'form/$', getform)`和`url(r'formadmin/', admin)`，
  * 实际上在访问formadmin的时候，实际访问的是form页面。
  * 解决办法是加入行尾匹配符：`url(r'form/$', getform)`和`url(r'formadmin/', admin)`





## 一个简单的 URLconf:
```py
from django.urls import path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
```

注意：
1. 要从 URL 中取值，使用尖括号。
2. 捕获的值可以选择性地包含转换器类型。比如，使用 <int:name> 来捕获整型参数。如果不包含转换器，则会匹配除了 / 外的任何字符。
3. 这里不需要添加反斜杠，因为每个 URL 都有。比如，应该是 articles 而不是 /articles 。

一些请求的例子：
1. `/articles/2005/03/` 会匹配 URL 列表中的第三项。
   1. Django 会调用函数 `views.month_archive(request, year=2005, month=3) `。
2. `/articles/2003/` 将匹配列表中的第一个模式不是第二个，因为模式按顺序匹配，第一个会首先测试是否匹配。请像这样自由插入一些特殊的情况来探测匹配的次序。在这里 
   1. Django 会调用函数 `views.special_case_2003(request)`.
3. `/articles/2003` 不匹配任何一个模式，因为每个模式要求 URL 以一个斜线结尾。
4. `/articles/2003/03/building-a-django-site/` 会匹配 URL 列表中的最后一项。
   1. Django 会调用函数 `views.article_detail(request, year=2003, month=3, slug="building-a-django-site") `。


## 路径转换器
下面的路径转换器在默认情况下是有效的：

* str - 匹配除了 '/' 之外的非空字符串。如果表达式内不包含转换器，则会默认匹配字符串。
* int - 匹配 0 或任何正整数。返回一个 int 。
* slug - 匹配任意由 ASCII 字母或数字以及连字符和下划线组成的短标签。比如，building-your-1st-django-site 。
* uuid - 匹配一个格式化的 UUID 。为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写。比如，075194d3-6885-417e-a8a8-6c931e272f00。返回一个 UUID 实例。
* path - 匹配非空字段，包括路径分隔符 '/' 。它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分。


## 注册自定义的路径转换器



## 使用正则表达式

使用 `re_path()` 而不是 `path()` 。

在 Python 正则表达式中，命名正则表达式组的语法是 `(?P<name>pattern)` ，其中 `name` 是组名， `pattern` 是要匹配的模式。
```py
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]
```

### 使用未命名的正则表达式组
### 嵌套参数




## URLconf 在什么上查找
请求的URL被看做是一个普通的Python 字符串， URLconf在其上查找并匹配。进行匹配时将不包括GET或POST请求方式的参数以及域名。

例如， https://www.example.com/myapp/ 请求中，URLconf 将查找 myapp/

在 https://www.example.com/myapp/?page=3 请求中，URLconf 仍将查找 myapp/ 。

URLconf 不检查使用了哪种请求方法。换句话讲，所有的请求方法 —— 即，对同一个URL的无论是 POST请求 、 GET请求 、或 HEAD 请求方法等等 —— 都将路由到相同的函数。





## 指定视图参数的默认值


```py
# URLconf
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.page),
    path('blog/page<int:num>/', views.page),
]

# View (in blog/views.py)
def page(request, num=1):
    # Output the appropriate page of blog entries, according to num.
    pass

```

在上面的例子中，两个URL模式都指向了相同的视图—— views.page 但是
* 第一个样式不能在URL中捕获到任意东西。
* 如果第一个URL模式去匹配URL，page() 函数会使用它默认参数 num=1。
* 如果第二个URL模式去匹配URL，page() 函数都会使用捕获到的任意 ``num``参数。





## 包含其它的URLconfs


```py
from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path('community/', include('aggregator.urls')),
    path('contact/', include('contact.urls')),
    # ... snip ...
]
```



### 精简包含

```py
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/history/', views.history),
    path('<page_slug>-<page_id>/edit/', views.edit),
    path('<page_slug>-<page_id>/discuss/', views.discuss),
    path('<page_slug>-<page_id>/permissions/', views.permissions),
]
```

我们可以改进它，通过只声明共同的路径前缀一次并将后面的部分分组:

```py
from django.urls import include, path
from . import views

urlpatterns = [
    path('<page_slug>-<page_id>/', include(
              [
                path('history/', views.history),
                path('edit/', views.edit),
                path('discuss/', views.discuss),
                path('permissions/', views.permissions),
              ]
          )
        ),
]
```




### 捕获的参数
被包含的URLconf 会收到来自父URLconf 捕获的任何参数，所以下面的例子是合法的:
```py
# In settings/urls/main.py
from django.urls import include, path

urlpatterns = [
    path('<username>/blog/', include('foo.urls.blog')),
]

# In foo/urls/blog.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog.index),
    path('archive/', views.blog.archive),
]
```


在上面的例子中，捕获的 "username" 变量将被如期传递给include()指向的URLconf。






## 传递额外选项给视图函数
URLconfs 有钩子来允许你把其他参数作为 Python 字典来传递给视图函数。

path() 函数可带有可选的第三参数（必须是字典），传递到视图函数里。

例如:
```py
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
]
```
在这个例子里，当请求到 `/blog/2005/` 时，Django 将调用 `views.year_archive(request, year=2005, foo='bar')` 。



### 传递额外选项给 include()
同样的，你可以额外其他选项给 include() ，并且已包含的 URLconf 里的每一行将被传递额外选项。

例如，下面两个 URLconf 配置在功能上是相同的：

配置一：
```py
# main.py
from django.urls import include, path

urlpatterns = [
    path('blog/', include('inner'), {'blog_id': 3}),
]

# inner.py
from django.urls import path
from mysite import views

urlpatterns = [
    path('archive/', views.archive),
    path('about/', views.about),
]
```

配置二：
```py
# main.py
from django.urls import include, path
from mysite import views

urlpatterns = [
    path('blog/', include('inner')),
]

# inner.py
from django.urls import path

urlpatterns = [
    path('archive/', views.archive, {'blog_id': 3}),
    path('about/', views.about, {'blog_id': 3}),
]
```

注意额外的选项会一直传递给所包含的 URLconf 的每一行，不管视图是否接受这些额外选项。因此，这个技巧仅在确定所包含的 URLconf 中的每一个视图接受你传递的额外选项时有用。






## URL 的反向解析

强烈建议不要硬编码 URL（这是一个费力、不能扩展、容易出错的主意）。同样危险的是设计临时机制来生成的 URL 与URLconf描述的设计的URL一样，这会导致 URL 随着时间的推移变得过时。

Django 提供了一个解决方案，使得 URL 映射是 URL 设计唯一的仓库。你使用 URLconf 来填充它，然后可以双向使用它：
1. 从用户/浏览器请求的 URL 开始，它调用正确的Django视图，并从 URL 中提取它的参数需要的值。
2. 从相应的 Django 视图标识以及要传递给它的参数来获取相关联的 URL 。


Django 提供执行反转 URL 的工具，这些工具与需要 URL 的不同层匹配：
1. 在模板里：使用 url 模板标签。
2. 在 Python 编码：使用 reverse() 函数。
3. 在与 Django 模型实例的 URL 处理相关的高级代码中： get_absolute_url() 方法。

```py
from django.urls import path

from . import views

urlpatterns = [
    #...
    path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    #...
]
```
根据这个设计，与 year nnnn 相对应的 URL 是 `/articles/<nnnn>/` 。


可以使用以下方式在模板代码中来获取它们：
```py
<a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
{# Or with the year in a template context variable: #}
<ul>
  {% for yearvar in year_list %}
    <li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
  {% endfor %}
</ul>
```

或在 Python 代码里：
```py
from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))
```


如果决定改变每年已发布的文章存档内容的 URL ，你只需要改变 URLconf 中的条目即可。

在一些视图具有一般性质的场景下，URLs 和视图存在多对一关系。对于这些情况，当反转 URLs 时，视图名并不是一个足够好的标识符。



## 命名 URL 模式







## URL 命名空间

### 介绍


### 反向命名空间 URLs



### URL 命名空间和包含的 URLconfs

