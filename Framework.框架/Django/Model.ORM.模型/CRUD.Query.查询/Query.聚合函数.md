# ORM select 聚合函数

1. Sum
2. Avg
3. Count
4. max/min


| id  | name | age |
| --- | ---- | --- |
| 1   | 张三 | 23  |
| 2   | 李四 | 22  |
| 3   | 王五 | 20  |

| id  | student_name | subject_name | score | year | student_id |
| --- | ------------ | ------------ | ----- | ---- | ---------- |
| 1   | 张三         | 语文         | 98.0  | 2000 | 1          |
| 2   | 张三         | 数学         | 92.0  | 2000 | 1          |
| 3   | 张三         | 英语         | 90.0  | 2000 | 1          |
| 4   | 李四         | 语文         | 89.0  | 2000 | 2          |
| 5   | 李四         | 数学         | 99.0  | 2000 | 2          |
| 6   | 李四         | 英语         | 67.0  | 2000 | 2          |
| 7   | 王五         | 语文         | 88.0  | 2000 | 3          |
| 8   | 王五         | 数学         | 87.0  | 2000 | 3          |
| 9   | 王五         | 英语         | 99.0  | 2000 | 3          |


#### aggregate 返回一个结果
#### annotate 在列表中使用，返回多个结果






views.py
```py
def page_grade(request):
    grade_list = Grade.objects.filter(student_name='张三')
    total = grade_list.aggregate(Sum('score'))
    print(total)
    total1 = grade_list.aggregate(total_score=Sum('score'))
    print(total1)

    stu_list = Student.objects.annotate(Sum('stu_grade__score'))
    stu_list1 = Student.objects.annotate(total=Sum('stu_grade__score'))

    return render(request, 'page_grade.html', {
        'total': total,
        'total1': total1,
        'stu_list': stu_list,
        'stu_list1': stu_list1,
    })
```

page_grade.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>聚合 统计</title>
</head>
<body>

    <h3>练习1： 求某个学生期末成绩的总和</h3>
    <p>张三的期末成绩总分： {{ total1.total_score }}</p>
    <p>张三的期末成绩总分： {{ total.score__sum }}</p>

    <h3>练习2：求某一科目成绩的最高分/最低分</h3>

    <h3>练习3：求某一科目成绩的平均分</h3>

    <h3>练习4：求每个学生期末成绩的总和</h3>
        {% for stu in stu_list %}
            <p>{{ stu.name }}: {{ stu.stu_grade__score__sum }}</p>
        {% endfor %}
        {% for stu in stu_list1 %}
            <p>{{ stu.name }}: {{ stu.total }}</p>
        {% endfor %}
</body>
</html>
```

urls.py
```py
from django.urls import path, include

from grade.views import page_grade

urlpatterns = [
    path('aggregate/', page_grade),
]
```

```url
http://127.0.0.1:8000/grade/aggregate/
```

