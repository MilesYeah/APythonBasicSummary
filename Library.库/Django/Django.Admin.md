# Django admin




## Admin

什么是Admin
* Admin是Django自带的一个功能强大的自动化数据管理界面
* 被收钱的用户可直接在Admin中管理数据库
* Django提供了许多针对Admin的定制功能

配置Admin
- 创建用户
    - cmd: `python manage.py createsuperuser`
    - 以建立admin/Aa123456超级用户
    - 访问后台管理系统: <localhost:8000/admin>
    - 修改settings.py中的LANGUAGE_CODE改为 zh_Hans ，即可将admin管理界面的语言改为中文
 - 配置应用
    - 在应用下admin.py中引入自身的models模块（或里面的模型类）
    - 编辑admin.py： `admin.site.register(models.Article)`

一个创建例子：
```
D:\OneDrive\Programming\Python\Django\blog_imooc>python manage.py createsuperuser
用户名 (leave blank to use 'itach'): root
电子邮件地址: admin@admin.com
Password:
Password (again):
这个密码太常见了。
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```



## admin配置类

* 声明：`class ArticleAdmin(admin.ModelAdmin)`
* 注册：`admin.site.register(Article, ArticleAdmin)`

Sample
``` python admin.py
from django.contrib import admin
from blog.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time', )
    pass


admin.site.register(Article, ArticleAdmin)

```


### admin页面中显示其他字段
* `list_display = ('param1', 'param2')`
* list_display同时支持tuple和list

### admin过滤器
* `list_filter = ( 'param1', )`

