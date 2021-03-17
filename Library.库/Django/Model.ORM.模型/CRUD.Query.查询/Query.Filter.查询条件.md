# ORM Query.Filter.查询条件



## 相等/等于
◆exact——等于**值（默认的形式）
如：id exact=6或者id=6
◆iexact——像**值
如：name_iexact=zhangsan'
#name LIKE‘zhangsan'

```py
>>> users = User.objects.filter(id=6)
>>> users1 = User.objects.filter(id__exact=6)
>>> users2 = User.objects.filter(username__exact='username_3')
>>> 
>>> users[0].username
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`id` = 6 LIMIT 1; args=(6,)
'username_3'
>>> users1[0].username
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`id` = 6 LIMIT 1; args=(6,)
'username_3'
>>> users2[0].username
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` = 'username_3' LIMIT 1; args=('username_3',)
'username_3'
>>>
```


```py
>>> users3 = User.objects.filter(username__iexact='username_3')
>>>
>>> users3[0].username
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` LIKE 'username\\_3' LIMIT 1; args=('username\\_3',)
'username_3'
>>>
```



## 布尔条件
◆gt——大于某个值
◆gte——大于或等于某个值
◆lt——小于某个值
◆lte——小于或等于某个值
◆isnull是否为空值



```py
>>> users = User.objects.filter(status__gt=0)
>>> users
(0.016) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`status` > 0 LIMIT 21; args=(0,)
<QuerySet [<User: User: username_8>, <User: User: username_9>, <User: User: username_10>, <User: User: username_11>, <User: User: username_12>, <User: User: username_13>, <User: User: username_14>, <User: User: username_15>, <User: User: username_16>, <User: User: username_17>, <User: User: username_18>, <User: User: username_19>, <User: User: username_20>, <User: User: username_21>, <User: User: username_22>, <User: User: username_23>, <User: User: username_24>, <User: User: username_25>, <User: User: username_26>, <User: User: username_27>, '...(remaining elements truncated)...']>
>>>
>>> users = User.objects.filter(status__gte=0)
>>> users
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`status` >= 0 LIMIT 21; args=(0,)
<QuerySet [<User: User: lisi>, <User: User: username_0>, <User: User: username_1>, <User: User: username_2>, <User: User: username_3>, <User: User: username_4>, <User: User: username_5>, <User: User: username_6>, <User: User: username_7>, <User: User: username_8>, <User: User: username_9>, <User: User: username_10>, <User: User: username_11>, <User: User: username_12>, <User: User: username_13>, <User: User: username_14>, <User: User: username_15>, <User: User: username_16>, <User: User: username_17>, <User: User: username_18>, '...(remaining elements truncated)...']>
>>>
>>>
>>> users = User.objects.filter(nickname__isnull=True).count()
(0.000) SELECT COUNT(*) AS `__count` FROM `account_user` WHERE `account_user`.`nickname` IS NULL; args=()
>>> users
1
>>>
```



## 是否包含**字符串
1. contains——包含**值如：name_contains=‘san'
2. icontains——包含**值，不区分大小写如：name contains=‘san'   #ZhangSan zhangsan 都满足条件
3. 在**选项（列表）之内   in
4. 以**开始 startswith、istartswith
5. 以**结束 endswith、iendswith


```py
>>> User.objects.filter(username__contains='user').count()
(0.000) SELECT COUNT(*) AS `__count` FROM `account_user` WHERE `account_user`.`username` LIKE BINARY '%user%'; args=('%user%',)
100
>>>
>>> User.objects.filter(username__icontains='user').count()
(0.000) SELECT COUNT(*) AS `__count` FROM `account_user` WHERE `account_user`.`username` LIKE '%user%'; args=('%user%',)
100
>>>
```


```py
>>> User.objects.filter(username__in=['abc', 'lisi'])
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` IN ('abc', 'lisi') LIMIT 21; args=('abc', 'lisi')
<QuerySet [<User: User: abc>, <User: User: lisi>]>
>>>
```


```py
>>> User.objects.filter(username__startswith='user')
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` LIKE BINARY 'user%' LIMIT 21; args=('user%',)
<QuerySet [<User: User: username_0>, <User: User: username_1>, <User: User: username_2>, <User: User: username_3>, <User: User: username_4>, <User: User: username_5>, <User: User: username_6>, <User: User: username_7>, <User: User: username_8>, <User: User: username_9>, <User: User: username_10>, <User: User: username_11>, <User: User: username_12>, <User: User: username_13>, <User: User: username_14>, <User: User: username_15>, <User: User: username_16>, <User: User: username_17>, <User: User: username_18>, <User: User: username_19>, '...(remaining elements truncated)...']>
>>>
>>> User.objects.filter(username__endswith='6')
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` LIKE BINARY '%6' LIMIT 21; args=('%6',)
<QuerySet [<User: User: username_6>, <User: User: username_16>, <User: User: username_26>, <User: User: username_36>, <User: User: username_46>, <User: User: username_56>, <User: User: username_66>, <User: User: username_76>, <User: User: username_86>, <User: User: username_96>]>
>>>
```




## 日期及时间
·date—日期Co
◆year—年
◆month——月份
◆day—天o
◆hour/minute/second——时分秒
◆week/week_day——星期



```py
>>> from datetime import datetime
>>> d = datetime(2025, 6, 11)
>>> User.objects.filter(updated_at__date=d)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE DATE(`account_user`.`updated_at`) = '2025-06-11' LIMIT 21; args=('2025-06-11',)
<QuerySet [<User: User: username_0>]>
>>>
>>> User.objects.filter(updated_at__date=datetime(2026, 3, 11))
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE DATE(`account_user`.`updated_at`) = '2026-03-11' LIMIT 21; args=('2026-03-11',)
<QuerySet [<User: User: lisi>]>
>>>
>>>
```


```py
>>> User.objects.filter(updated_at__day=16)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE EXTRACT(DAY FROM `account_user`.`updated_at`) = 16 LIMIT 21; args=(16,)
<QuerySet [<User: User: username_2>, <User: User: username_3>]>
>>>
>>> User.objects.filter(updated_at__year=2018)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`updated_at` BETWEEN '2018-01-01 00:00:00' AND '2018-12-31 23:59:59.999999' LIMIT 21; args=('2018-01-01 00:00:00', '2018-12-31 23:59:59.999999')
<QuerySet [<User: User: username_3>]>
>>>
```



## 外键关联查询
◆查询在线问答系统中某个用户的回答 filter(user__username='张三)


User
| id  | created_at                 | updated_at                 | username | password | nickname | avatar | status | is_super |
| --- | -------------------------- | -------------------------- | -------- | -------- | -------- | ------ | ------ | -------- |
| 1   | 2021-03-12 00:53:00.300743 | 2021-03-12 00:53:00.300743 | haha     | 123456   | ha       |        | 0      | 0        |
| 2   | 2021-03-12 00:53:11.052314 | 2021-03-12 00:53:11.052314 | zhangsan | 123456   | an       |        | 0      | 0        |
| 3   | 2021-03-12 00:53:17.566339 | 2021-03-12 00:53:17.566339 | lisi     | 123456   | si       |        | 1      | 0        |
| 4   | 2021-03-12 00:53:24.018843 | 2021-03-12 00:53:24.018843 | wangwu   | 123456   | wu       |        | 1      | 0        |
| 5   | 2021-03-12 00:53:30.352590 | 2021-03-12 00:53:30.352590 | zhaoliu  | 123456   | iu       |        | 1      | 0        |

UserProfile
| id  | created_at                 | updated_at                 | username | real_name | sex | maxim | address | user |
| --- | -------------------------- | -------------------------- | -------- | --------- | --- | ----- | ------- | ---- |
| 1   | 2021-03-12 00:53:00.304734 | 2021-03-12 00:53:00.304734 | haha     |           | 0   |       |         | 1    |
| 2   | 2021-03-12 00:53:11.055276 | 2021-03-12 00:53:11.055276 | zhangsan |           | 0   |       |         | 2    |
| 3   | 2021-03-12 00:53:17.570329 | 2021-03-12 00:53:17.570329 | lisi     |           | 0   |       |         | 3    |
| 4   | 2021-03-12 00:53:24.023829 | 2021-03-12 00:53:24.023829 | wangwu   |           | 0   |       |         | 4    |
| 5   | 2021-03-12 00:53:30.355583 | 2021-03-12 00:53:30.355583 | zhaoliu  |           | 0   |       |         | 5    |

UserProfile 表的 user 字段关联了 User 表.
所以, 查询到时候可以使用 `user__nickname__contains` 这种语句来查询,其意思就是, `user` 表下的 `nickname` 字段 `contains` 包含什么什么字符串的条件

```py
>>> UserProfile.objects.filter(user__nickname="wu")
(0.000) SELECT @@SQL_AUTO_IS_NULL; args=None
(0.000) SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; args=None
(0.016) SELECT `account_user_profile`.`id`, `account_user_profile`.`created_at`, `account_user_profile`.`updated_at`, `account_user_profile`.`user`, `account_user_profile`.`username`, `account_user_profile`.`real_name`, `account_user_profile`.`sex`, `account_user_profile`.`maxim`, `account_user_profile`.`address` FROM `account_user_profile` INNER JOIN `account_user` ON (`account_user_profile`.`user` = `account_user`.`id`) WHERE `account_user`.`nickname` = 'wu' LIMIT 21; args=('wu',)
<QuerySet [<UserProfile: UserProfile object (4)>]>
>>>
```
```py
>>> UserProfile.objects.filter(user__nickname__contains="u")
(0.000) SELECT `account_user_profile`.`id`, `account_user_profile`.`created_at`, `account_user_profile`.`updated_at`, `account_user_profile`.`user`, `account_user_profile`.`username`, `account_user_profile`.`real_name`, `account_user_profile`.`sex`, `account_user_profile`.`maxim`, `account_user_profile`.`address` FROM `account_user_profile` INNER JOIN `account_user` ON (`account_user_profile`.`user` = `account_user`.`id`) WHERE `account_user`.`nickname` LIKE BINARY '%u%' LIMIT 21; args=('%u%',)
<QuerySet [<UserProfile: UserProfile object (4)>, <UserProfile: UserProfile object (5)>]>
>>>
```



## 多个条件同时满足
### filter的深入使用

```py
>>> User.objects.filter(username__contains='a')
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE `account_user`.`username` LIKE BINARY '%a%' LIMIT 21; args=('%a%',)
<QuerySet [<User: User: haha>, <User: User: zhangsan>, <User: User: wangwu>, <User: User: zhaoliu>]>
>>>
>>>
>>> User.objects.filter(username__contains='a').filter(status=1)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`username` LIKE BINARY '%a%' AND `account_user`.`status` = 1) LIMIT 21; args=('%a%', 1)
<QuerySet [<User: User: wangwu>, <User: User: zhaoliu>]>
>>>
```

```py
>>> User.objects.filter(username__contains='a', status=1)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`status` = 1 AND `account_user`.`username` LIKE BINARY '%a%') LIMIT 21; args=(1, '%a%')
<QuerySet [<User: User: wangwu>, <User: User: zhaoliu>]>
>>>
```



### &运算符的使用

```py
>>> User.objects.filter(username__contains='a') & User.objects.filter(status=1)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`username` LIKE BINARY '%a%' AND `account_user`.`status` = 1) LIMIT 21; args=('%a%', 1)
<QuerySet [<User: User: wangwu>, <User: User: zhaoliu>]>
>>>
```



### Q()函数实现复杂的查询

Q()函数支持&（且）|（或），对应SQL中的AND和OR


```py
>>> from django.db.models import Q
>>> query = Q(username__contains='a', status=1)
>>> User.objects.filter(query)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`status` = 1 AND `account_user`.`username` LIKE BINARY '%a%') LIMIT 21; args=(1, '%a%')
<QuerySet [<User: User: wangwu>, <User: User: zhaoliu>]>
>>>
>>>
```

```py
>>> query = Q(username__contains='a') & Q(status=1)
>>> User.objects.filter(query)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`username` LIKE BINARY '%a%' AND `account_user`.`status` = 1) LIMIT 21; args=('%a%', 1)
<QuerySet [<User: User: wangwu>, <User: User: zhaoliu>]>
>>>
```




```py
>>> query = Q(username='zhaoliu') | Q(status=0)
>>> User.objects.filter(query)
(0.000) SELECT `account_user`.`id`, `account_user`.`created_at`, `account_user`.`updated_at`, `account_user`.`username`, `account_user`.`password`, `account_user`.`nickname`, `account_user`.`avatar`, `account_user`.`status`, `account_user`.`is_super` FROM `account_user` WHERE (`account_user`.`username` = 'zhaoliu' OR `account_user`.`status` = 0) LIMIT 21; args=('zhaoliu', 0)
<QuerySet [<User: User: haha>, <User: User: zhangsan>, <User: User: zhaoliu>]>
>>>
```



