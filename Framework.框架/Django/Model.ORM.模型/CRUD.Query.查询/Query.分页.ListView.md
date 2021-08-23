# ORM select 分页

1. QuerySet 切片
2. Paginator
3. ListView





## ListView

view.py
```py
class UserListView(ListView):
    template_name = 'page_split_listview.html'
    model = User
    paginate_by = 10
    page_kwarg = 'p'

```

urls.py
```py
from django.urls import path
from account import views

urlpatterns = [
    path('split_pages/listview/', views.UserListView.as_view()),

]
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List View</title>
</head>
<body>
    <h2>Split Slice</h2>
    <p>统计：共 {{ page_obj.paginator.num_pages }} 页，当前第 {{ page_obj.number }} 页</p>
    {% for i in object_list %}
        <p>{{ i.id }} : {{ i.username }}</p>
    {% endfor %}
</body>
</html>
```

```url
http://127.0.0.1:8000/account/split_pages/listview/?p=2
```

