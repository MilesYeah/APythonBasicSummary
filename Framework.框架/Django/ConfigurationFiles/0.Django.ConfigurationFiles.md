# Django configuration files


## Project folder and files

* manage.py
  * 项目管理器，
  * 他是与项目进行交互的命令行工具集的入口，
  * 执行`python manage.py`来查看所有的命令。

* templates: 存放HTML模板文件

* project folder: %proj%
  * 作用：
    * 项目的容器，
    * 包含项目最基本的一些配置，
    * 他的目录名称是不建议修改的，但Django是允许修改的。
    * 因为在初始化的时候很多配置都是依赖于这个目录名称的，如果实在是需要改的话，那么就要将所有的路径引用都修改一下。

  * %proj%/settings.py
    * BASE_DIR    项目根目录
    * SECRET_KEY  
    * DEBUG   模式，如果打开则所有的debug信息输出在屏幕上
    * ALLOWED_HOSTS   
    * INSTALLED_APPS  所有的应用都需要添加在这个列表里
    * MIDDLEWARE  中间键，是Django自带的一些工具集
    * ROOT_URLCONF    URL根文件的配置文件
    * TEMPLATES   模板，其实就是一个一个的html文件，其实就是关于模板的一些配置
    * WSGI_APPLICATION    
    * DATABASES   默认使用sqlite3，如果使用其他的数据库，可以根据上面注释中提供出来的网页查阅如何配置其他的db
    * AUTH_PASSWORD_VALIDATORS    密码认证相关
    * LANGUAGE_CODE = 'en-us'     如果想要使用中文，则使用“zh_hans”（简体）或者“zh_hant”（繁体）
    * TIME_ZONE = 'UTC'
    * USE_I18N = True
    * USE_L10N = True
    * USE_TZ = True

  * %proj%/urls.py
    * Url配置文件
    * Django项目中所有的地址（页面）都需要我们自己去配置器URL
    * 每个URL都以url的形式写出来
    * url函数放在urlpatterns列表中
    * url函数三个参数：URL，对应方法，名称

  * %proj%/wsgi.py
    * Python Web Server Gateway Interface, 
    * Python服务器网关接口，
    * 他是Python应用于Web服务器之间的接口。

* 除此之外，我们还需要建立如下文件夹（对于大项目）
  * static: 存放项目所需的静态文件，如CSS,图片等
  * log： 存放项目运行的日志文件
  * media： 存放用户上传的文件
  * apps：
    * 当项目下有很多个app时，此时如果全都将app放在project根目录下的话会显得很乱，此时可建立该文件夹将app全都存放该目录下。
    * 注意apps这个目录下建立一个__init__.py让他成为一个包。
    * 可是每当想要引用apps下的app时，每次都要写入from apps.app import，如果觉得麻烦，可以在settings.py中奖BASE_DIR改为apps所在目录即可。


## Application folder and files

* migirations
  * 数据移植（迁移）的模块
  * 其内容都是Django自动生成的

* admin.py
  * 该应用的后台管理系统配置文件
  * 每个应用下都有自己的配置文件

* apps.py
  * 当前应用的一些配置
  * Django1.9之后才会自动生成

* models.py
  * 数据模块，通常是数据库
  * 使用ORM框架
  * 类似MVC结构中的Models（模型）

* test.py
  * 自动化测试模块
  * Django提供了自动化测试功能
  * 在这里编写测试脚本

* views.py
  * 执行相应的代码所在模块
  * 代码逻辑处理的主要地点
  * 项目中的**大部分**代码都是在这里编写
  * 每个响应对应一个函数，函数必须返回一个响应
  * 函数必须存在一个参数，一般约定为request
  * 每个响应（函数）对应一个URL


