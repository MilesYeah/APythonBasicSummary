# ORM select 分页

1. QuerySet 切片
2. Paginator
3. ListView

使用Paginator进行分页
◆步骤一：取得分页器Paginator（objects，page_size）
步骤二：取得页面实例page=p.page（page_num）

分页处理相关类
◆Paginator—分页器
Page——某一页对象
·异常
InvalidPage无效的页码
√PageNotAnlnteger——页码必须是整数
√EmptyPage——空页（没有数据）


◆步骤一：取得分页器Paginator（objects，page_size）
√objects——要进行分页的数据
√page_size——每页的数据多少
>>p=Paginator（objects，2）


Paginator的属性
·count——数据记录的总条数
◆num_pages——总页数（总记录条数/每页大小）
◆page_range——页码范围


◆步骤二：取得页面实例page=p.page（page_num）
page_num——当前页的页码，如第几页
>p=Pagnator（obyects，2）
>>page=p.page（3）

页面实例的属性
◆number——当前页的页码
◆object_list——当前页的数据列表
◆paginator——分页器对象的引用


页面实例的常用方法
.on has_next（）O是否还有下一页
has_previous（）——是否还有上一页
◆has_other_pages（）——是否还有其他页（上/下一页）
next_page_number（）——下一页的页码，如果没有，触发InvalidPage异常
next_page_number（）——上一页的页码，如果没有，触发InvalidPage异常





## Paginator
```py
Paginator(objects, page_size)
page = Paginator(User.objects.all(), 15)    # 每页15个元素
p = page(2)     # 拿到第二页数据
```

即使传入的页数不是整数 Paginator 也支持了默认的处理

异常
1. InvalidPage： 无效页码
2. PageNotAnInteger：
3. EmptyPage：


views.py
```py
def split_pages_paginator(request):
    page = int(request.GET.get('page', 1))
    page_size = 10

    obj = Paginator(User.objects.all(), page_size)

    items = obj.get_page(page)
    return render(request, 'page_split_paginator.html', {"items": items})
```

urls.py
```py
from django.urls import path
from account import views

urlpatterns = [
    path('split_pages/paginator/', views.split_pages_paginator),

]
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>page_split_paginator</title>
</head>
<body>
    <h2>Split Slice</h2>
    <p>统计：共 {{ items.paginator.num_pages }} 页，当前第 {{ items.number }} 页</p>
    {% for i in items.object_list %}
        <p>{{ i.id }} : {{ i.username }}</p>
    {% endfor %}
</body>
</html>
```

```url
http://127.0.0.1:8000/account/split_pages/paginator/?page=2
```

