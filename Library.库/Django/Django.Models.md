# Django models

存放在app目录下。


----------------------------------------------------------------------------------------------------
## Definations

```python
class UserMessage(models.Models):
    name = models.CharField(max_length=20, verbose_name='用户名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=100, verbose_name='联系地址')
    message = models.CharField(max_length=500, verbose_name='留言信息')

    class Meta:
        verbose_name = '用户留言信息'
        verbose_name_plural = verbose_name      # 后台显示的附属信息
        db_table = 'user_table'     # 可以指定生成表的时候，表的名字
        ordering = '-name'       # 默认的排序，前面加一个-可以指定默认排序为倒序排序

```


### 数据类型
常用数据类型:
* models.CharField
* models.EmailField
* models.CharField
* models.CharField
* models.ForeignKey
* models.IPAddressField
* models.IntegerField
* models.FileField
* models.ImageField
* models.CharField


----------------------------------------------------------------------------------------------------
## Models

* 通常，一个model对应数据库的一张数据表，
* Django中Models以类的形式出现，
* 包含了一些基本字段以及一些数据的一些行为

ORM 
* 对象关系映射，Object Relation Mapping
* 实现了对象和数据库之间的映射
* 隐藏了数据访问的细节，不需要编写SQL语句

编写Models
* 建立文件
  * 在应用根目录下创建 models.py, 并引入models模块
  * 创建类，继承models.Model，该类即是一张数据表
  * 在类中创建字段

* 建立字段
  * 字段即类里面的属性（变量）
  * attr = models.CharField(max_length=64)

* 生成数据表
  * 命令行中进入manage.py同级目录
  * 执行`python manage.py makemigrations [%app_name%]`
  * 再执行`python manage.py migrate`

* 查看生成的数据表
  * Django会自动在app/migrations/目录下生成移植文件
  * 执行`python manage.py sqlmigrate %app_name% %file_id%`查看sql语句
  * 默认sqlite3的数据库在项目根目录下db.sqlite3


查看并编辑db.sqlite3
* 使用第三方软件
* SQLite Expert Personal
* 轻量级，完全免费



----------------------------------------------------------------------------------------------------
## 数据库的增删改查

### 增

UserMessage.objects.create()
  * 在数据库中创建一个UserMessage记录

UserMessage.objects.save()
  * 当建立好对象之后，可以直接使用对象的objects.save方法将数据存储在数据库中。

### 删


### 改


### 查

UserMessage.objects.all()
  * 将数据库中所有的数据都取出来。

UserMessage.objects.filter(name='bob', address='北京')
  * 从数据库中取出北京的bob的数据




### 常用方法






----------------------------------------------------------------------------------------------------
## Command cheat sheet

python manage.py makemigrations
python manage.py migrate

