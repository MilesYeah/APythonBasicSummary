# 开发一个 get post 接口请求

完整的项目目录结构
```bat
PS G:\Mirror\SourceCode\trials\tryDjango> tree /f .
Folder PATH listing for volume 1.9T.2
Volume serial number is 70A2-7D0A
G:\MIRROR\SOURCECODE\TRIALS\TRYDJANGO
│   db.sqlite3
│   manage.py
│
├───get_post
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │       __init__.py
│   │
│   └───templates
│           get.html
│           post.html
│           result.html
│
└───tryDjango
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py

PS G:\Mirror\SourceCode\trials\tryDjango> 
```





## get_post
### html 渲染文件
```html
{#\tryDjango\get_post\templates\get.html#}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Get</title>
</head>
<body>
    <!-- action 和 urls 中的 re_path(r'^result_get/$', views.result_get) 呼应 -->
    <!-- 浏览器跳转之后，需要使用到该地址 -->
    <form action="/get_post/result_get" method="get">
        <!-- input 标签的 q 将作为 get 的参数传递到 Django view 函数的 request.GET 字典中 -->
        <input type="text" name="q" />
        <input type="submit" value="搜索" />
    </form>
</body>
</html>
```


```html
{#\tryDjango\get_post\templates\post.html#}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Post</title>
</head>
<body>
    <!-- action 和 urls 中的 re_path(r'^result_post/$', views.result_post) 呼应 -->
    <!-- 浏览器跳转之后，需要使用到该地址 -->
    <form action="/get_post/result_post/" method="post"> 
        {% csrf_token %}
        <!-- input 标签的 q 将作为 post 的参数传递到 Django view 函数的 request.POST 字典中 -->
        <input type="text" name="q" />
        <input type="submit" value="搜索" />
    </form>
</body>
</html>
```

```html
{#\tryDjango\get_post\templates\result.html#}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Result</title>
</head>
<body>
    <h1>{{ result }}</h1>

</body>
</html>
```


### \tryDjango\get_post\urls.py
```py
# \tryDjango\get_post\urls.py

from django.urls import path, re_path

from get_post import views

urlpatterns = [
    re_path(r'^input_get/$', views.input_get),
    re_path(r'^result_get/$', views.result_get),        # 该地址即为 get.html 中的form action 地址
    re_path(r'^input_post/$', views.input_post),
    re_path(r'^result_post/$', views.result_post),      # # 该地址即为 post.html 中的form action 地址

]

```


### \tryDjango\get_post\views.py

```py
# \tryDjango\get_post\views.py
from django.shortcuts import render, HttpResponse


def input_get(request):
    return render(request, "get.html")           # 引用 get.html,用于获取一个输入值


def result_get(request):
    context = {}
    context['result'] = f"Searching result(POST): {request.GET['q']}"       # 使用 get.html 获取到输入值之后，获取到这个输入值
    return render(request, "result.html", context)                          # 使用 result.html 联合上述获取到的输入值在浏览器中渲染出效果


def input_post(request):
    return render(request, "post.html")                         # 引用 post.html,用于获取一个输入值


def result_post(request):
    context = {}
    context['result'] = f"Searching result(POST): {request.POST['q']}"      # 使用 get.html 获取到输入值之后，获取到这个输入值
    return render(request, "result.html", context)                          # 使用 result.html 联合上述获取到的输入值在浏览器中渲染出效果

```





## tryDjango
### \tryDjango\tryDjango\settings.py

注册 get_post APP

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "get_post"                          # 注册 get_post APP
]
```


### \tryDjango\tryDjango\urls.py

囊括 get_post 中的 url
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path("get_post/", include("get_post.urls"))     # 导入 get_post app 中的 url 配置
]
```





## 执行结果

```ps1
python.exe .\manage.py runserver

```


### Get
1. 浏览器地址栏输入如下地址 http://127.0.0.1:8000/get_post/input_get/
2. 在弹出页面填写 `HTTPBasicAuth`
3. 浏览器跳转到如下地址 http://127.0.0.1:8000/get_post/result_get/?q=HTTPBasicAuth
4. 跳转后的页面显示    `Searching result(POST): HTTPBasicAuth`


### Post
1. 浏览器地址栏输入如下地址 http://127.0.0.1:8000/get_post/input_post/
2. 在弹出页面填写 `This is input post`
3. 浏览器跳转到如下地址 http://127.0.0.1:8000/get_post/result_post/
4. 跳转后的页面显示: `Searching result(POST): This is input post`

