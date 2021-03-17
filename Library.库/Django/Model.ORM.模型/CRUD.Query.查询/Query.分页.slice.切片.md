# ORM select 分页

1. QuerySet 切片
2. Paginator
3. ListView




## 切片
```py
User.objects.all()[10, 20]
User.objects.all()[100, 110]
```

```py
page_size = 10
index_start = (int(page_size) - 1 ) * page_size
index_end = int(page_size) * page_size
```


```py
def split_pages_slice(request):
    page = int(request.GET.get('page', 1))

    page_size = 10
    start = (page - 1) * page_size
    end = page * page_size
    items = User.objects.all()[start:end]

    return render(request, 'page_split_slice.html', {"items": items})
```
注意异常：因为最大值可能超过结果集的最大长度。


urls.py
```py
from django.urls import path
from account import views

urlpatterns = [
    path('split_pages/slice/', views.split_pages_slice),
]
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Split Slice</title>
</head>
<body>
    <h2>Split Slice</h2>
    <p>统计：共  页，当前第  页</p>
    {% for i in items%}
        <p>{{ i.id }} : {{ i.username }}</p>
    {% endfor %}
</body>
</html>

```

```url
http://127.0.0.1:8000/account/split_pages/slice/?page=2
```

