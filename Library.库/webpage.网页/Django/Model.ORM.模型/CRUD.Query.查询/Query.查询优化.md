# ORM 查询优化

## 配置 logging 使查询时的 sql 语句都打印出来

```conf
# 把所有的日志信息输出到控制台。
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
             'propagate': True,
             'level': 'DEBUG',
        }
    },
}
```

## 使用 obj.query 查看 sql 语句




## 使用 django-debug-toolbar

[0.django-debug-toolbar.md](../../django-debug-toolbar/0.django-debug-toolbar.md)





## 优化查询结构 

### ·QuerySet.select_related()

将外键关联的对象查询合并到主查询，一次性查询结果，减少SQL执行的数量



```py
>>> user = User.objects.get(pk=2)
(0.000) SELECT @@SQL_AUTO_IS_NULL; args=None
(0.000) SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; args=None
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`id` = 2 LIMIT 21; args=(2,)
>>> profiles = UserProfile.objects.all()
>>> profiles
(0.000) SELECT `account_user_profile`.`id`, `account_user_profile`.`created_at`, `account_user_profile`.`updated_at`, `account_user_profile`.`user`, `account_user_profile`.`username`, `account_user_profile`.`real_name`, `account_user_profile`.`sex`, `account_user_profile`.`maxim`, `account_user_profile`.`address` FROM `account_user_profile` LIMIT 21; args=()
<QuerySet [<UserProfile: UserProfile object (1)>, <UserProfile: UserProfile object (2)>, <UserProfile: UserProfile object (3)>, <UserProfile: UserProfile object (4)>, <UserProfile: UserProfile object (5)>]>
>>>
```


```py
>>> profiles = UserProfile.objects.all().select_related('user')
>>> profiles
(0.000) SELECT `account_user_profile`.`id`, `account_user_profile`.`created_at`, `account_user_profile`.`updated_at`, `account_user_profile`.`user`, `account_user_profile`.`username`, `account_user_profile`.`real_name`, `account_user_profile`.`sex`, `account_user_profile`.`maxim`, `account_user_profile`.`address`, `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user_profile` INNER JOIN `account_user` ON (`account_user_profile`.`user` = `account_user`.`id`) LIMIT 21; args=()
<QuerySet [<UserProfile: UserProfile object (1)>, <UserProfile: UserProfile object (2)>, <UserProfile: UserProfile object (3)>, <UserProfile: UserProfile object (4)>, <UserProfile: UserProfile object (5)>]>
>>>
```




## 使用 sql 查询
```py
>>> user_list = User.objects.raw('select * from account_user')
>>> user_list
<RawQuerySet: select * from account_user>
>>>
```



## 获取数据库连接,游标,直接执行 sql

```py
# 使用 django 获取 数据库连接
from django.db import connection
cursor = connection.cursor()
cursor.execute('select * from account_user')
cursor_rets = cursor.fetchall()
```
