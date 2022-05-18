Django "知识点"

## django 请求的生命周期
1. 浏览器发起请求
2. 一般到网关层先，然后再转发请求到 web 服务器
3. 到 web 服务器，比如 uwsgi
4. 到 web 应用程序，先经过中间件
5. 到 url 路由层进行匹配
6. 匹配成功，到视图层，可能是视图函数，也可能是视图类
7. 视图层从 models 模型层操作数据，进行业务逻辑处理
8. 如果是 template，就通过模板引擎渲染
9. 如果是 drf，就会通过 serializer 序列化器进行序列化





## mtv mvc 的区别
* MVC
  * M：Model，模型，和数据库进行交互
  * V：View，视图，负责产生 Html 页面
  * C：Controller，控制器，接收请求，进行处理，与 M 和 V 进行交互，返回应答
* MTV
  * M：Model，模型，和 MVC 中的 M 功能相同，和数据库进行交互
  * V：view，视图，和 MVC 中的 C 功能相同，接收请求，进行处理，与 M 和 T 进行交互，返回应答
  * T：Template，模板，和 MVC 中的 V 功能相同，产生 Html 页面."





## 跨域请求Django是如何处理的？
使用第三方工具 django-cors-headers 即可彻底解决
1. 注册app
2. 添加中间件
3. 配置运行跨域请求方法





## 什么是ASGI，简述WSGI和ASGI的关系与区别？
* ASGI 是异步网关协议接口，支持 http2 和 WebSocket
* WSGI 是基于 HTTP 协议模式的，不支持 WebSocket
* ASGI 是对 WSGI的扩展





## 可以正则匹配的路由方法名叫什么
re_path





## 路径转换器有什么数据类型，默认是什么
* str - 匹配除了 '/' 之外的非空字符串；如果表达式内不包含转换器，则会默认匹配字符串
* int - 匹配 0 或任何正整数返回一个 int
* slug - 匹配任意由 ASCII 字母或数字、-、_组成的短标签比如，building-your-1st-django-site
* uuid - 匹配一个格式化的 UUID ，
  * 为了防止多个 URL 映射到同一个页面，必须包含破折号并且字符都为小写
  * 比如 075194d3-6885-417e-a8a8-6c931e272f00，函数参数会拿到一个 UUID 实例
* path - 匹配非空字段，包括路径分隔符 '/' ，它允许你匹配完整的 URL 路径而不是像 str 那样匹配 URL 的一部分





## 路由怎么包含子路由

```py
path("",include())

```


## 模型继承的是哪个类
类继承

```py
django.db.models.Model

```


## 怎么自定义数据表名

```py
class Meta: # 通过 db_table 自定义数据表名
    db_table = 'member'

```


## 怎么定义一个抽象模型类，有什么特点

```py
class Meta:
    # 当前模型类为抽象模型类，在迁移时不会创建表，仅仅是为了供其他类继承
    abstract = True

```


## migrate、makemigrations、sqlmigrate 的区别

* migrate 负责应用和撤销迁移数据库
* makemigrations 负责生成迁移文件
* sqlmigrate 展示迁移使用的 sql 语句






## 有什么常用的模型字段，对应的数据库字段是什么

```py
'AutoField': 'integer AUTO_INCREMENT',
'BooleanField': 'bool',
'CharField': 'varchar(%(max_length)s)',
'DateField': 'date',
'DateTimeField': 'datetime(6)',
'FileField': 'varchar(%(max_length)s)',
'IntegerField': 'integer',
'BigIntegerField': 'bigint',
'TextField': 'longtext',
'TimeField': 'time(6)',
'UUIDField': 'char(32)',
```






## 模型类的 get、filter 方法有什么区别
* filter(**kwargs)：根据条件过滤查询结果，返回的类型为 `QuerySet 实例`；
* get(**kwargs)：返回与所给筛选条件相匹配的记录，只返回一个结果。如果符合筛选条件的记录超过一个或者没有都会抛出错误，返回的类型为模型 `对象实例`；





## 模型类怎么完成 and、or 操作
前面的多个 filter() 方法实现的是过滤条件的 “AND” 操作，如果想实现过滤条件 “OR” 操作呢，就需要使用到 Django 为我们提供的 Q() 方法：

```py
from django.db.models import Q

Member.objects.all().filter(Q(name='spyinx-22') | Q(name='spyinx-11'))
<QuerySet [<Member: <spyinx-11, 18919885274>>, <Member: <spyinx-22, 18702966393>>]>

Member.objects.all().filter(Q(namecontains='spyinx-2') & Q(nameendswith='2'))
<QuerySet [<Member: <spyinx-2, 18627420378>>, <Member: <spyinx-22, 18702966393>>]>
```






## 视图函数有什么特点
* 视图函数的第一参数是 HttpRequest 对象
* HttpRequest 对象包含了请求的所有数据（请求头、请求体）
* 视图函数必须得返回一个 HttpResponse 对象或者其子类对象





## 怎么获取路径参数，怎么获取字符串参数，怎么获取请求体参数，怎么获取表单、文件数据，怎么获取请求头参数

### 路径参数
1. 在 url 路径中传递的参数 
2. 在请求实例方法中，使用关键字参数来接收


### 查询字符串参数
1. url ？后面的 key value 键值对参数，如：http://www.xxx.com/?key1=value1&key2=value2 
2. request.GET 获取 
3. request.GET 返回 QueryDict，类似于 python 中 dict 类型 
4. 可以使用['key1']、get('key1')，会返回具体的值，如果有多个相同 key 的键值对，获取的是最后一个 
5. getlist('key1')，获取相同 key 的多个值，返回 list 类型


### 请求体参数
json 
1. json 格式的参数会存放在 body 中，一般为字节类型 
2. json.loads(request.body)，返回 Python 中的数据类型（字典、嵌套字典的列表） json.loads(request.body)

www-form-urlencoded 
1. 一般在前端页面中使用表单录入的参数 b.request.POST 返回 QueryDict，类似于 python 中 dict 类型

file（multipart/data） 
1. 传递的文本参数可以使用 request.POST 去提取 
2. 传递的非文本参数（二进制文件）可以使用 request.FILES 去提取 
3. 如果传递纯粹的文件，request.body 去提取


### 请求头参数
1. 第一种方式：`request.headers['key1']`或者`.get('key1')` 
2. 第二种方式：`request.META['HTTP_AUTHORIZATION']` 
   1. 请求头参数的可以被转化为：HTTP*参数名大写 
   2. 如果参数名中含有-，会自动转换为*













## ref
* [Django "知识点"](https://www.yuque.com/poloyy/interview/qqcsug)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

