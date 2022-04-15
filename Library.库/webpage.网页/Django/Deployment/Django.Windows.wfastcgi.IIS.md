
## 安装IIS和CGI

打开服务器管理器，选择添加角色和功能，选择要添加的服务器角色（WEB服务器IIS），然后安装

IIS安装成功之后，然后安装CGI，再次选择添加角色和功能，找到之前安装的WEB服务器IIS，点击它。

在展开的选项里找到WEB服务器，点击它，找到应用程序开发点击在展开的列表里找到CGI，勾选，然后下一步，安装它。

安装好CGI之后，我们在浏览器里输入http://127.0.0.1  访问IIS，如果出现 IIS 默认页面，说明IIS安装成功。


## 安装Python3

在C盘建立python目录，然后从Python官网下载Windows版本的64位的Python安装包，并安装它。

并且安装好 Django 项目的依赖包.


## 安装wfastcgi

在Windows下，我们没法使用uwsgi，但我们可以使用wfastcgi替代它，打开CMD窗口，输入命令安装wfastcgi：
安装成功之后，通过下面命令启动它：

```bat
C:\WINDOWS\system32>workon trials
(trials) C:\Windows\System32>
(trials) C:\Windows\System32>pip install wfastcgi
Collecting wfastcgi
  Downloading https://files.pythonhosted.org/packages/fb/c7/c67ab1c936b6294c3692d891ff6d4df1b82254a98f00e2cb72083b1ad796/wfastcgi-3.0.0.tar.gz
Installing collected packages: wfastcgi
  Running setup.py install for wfastcgi ... done
Successfully installed wfastcgi-3.0.0
WARNING: You are using pip version 19.2.3, however version 21.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

(trials) C:\Windows\System32>wfastcgi-enable
Applied configuration changes to section "system.webServer/fastCgi" for "MACHINE/WEBROOT/APPHOST" at configuration commit path "MACHINE/WEBROOT/APPHOST"
"c:\users\itach\envs\trials\scripts\python.exe|c:\users\itach\envs\trials\lib\site-packages\wfastcgi.py" can now be used as a FastCGI script processor

(trials) C:\Windows\System32>
```


如上，启动成功之后，它会把Python路径和wfastcgi的路径显示出来，我们需要把这个路径复制出来，保存好，后边用得着。

`c:\users\itach\envs\trials\scripts\python.exe|c:\users\itach\envs\trials\lib\site-packages\wfastcgi.py`

注意：上面的路径，是由Python解释器的路径和“|”以及“wfastcgi.py”文件路径组成。





## 4、在IIS里添加项目网站

把我们本地项目源码上传到服务器相应的目录里。
比如: Django 项目源码的位置如下
```
G:\Mirror\SourceCode\trials\deploy_django
```

通过【控制面板】->【管理工具】打开IIS管理器。

添加网站
1. 网站名称: deploy_django
2. 物理路径: G:\Mirror\SourceCode\trials\deploy_django
3. IP地址: 127.0.0.1
4. 端口: 80


## 建立 web.config 文件

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <handlers>
            <add name="Python FastCGI" 
                 path="*" 
                 verb="*" 
                 modules="FastCgiModule" 
                 scriptProcessor="<Path to Python>\python.exe|<Path to Python>\lib\site-packages\wfastcgi.py" 
                 resourceType="Unspecified" 
                 requireAccess="Script"/>
        </handlers>
    </system.webServer>
    <appSettings>
        <add key="WSGI_HANDLER" value="django.core.wsgi.get_wsgi_application()" />
        <add key="PYTHONPATH" value="<Path to Django App>" />
        <add key="DJANGO_SETTINGS_MODULE" value="<Django App>.settings" />
    </appSettings>
</configuration>
```

替换实际变量
1. `scriptProcessor="<Path to Python>\python.exe|<Path to Python>\lib\site-packages\wfastcgi.py" `
   1. <Path to Python>\python.exe|<Path to Python>\lib\site-packages\wfastcgi.py
   2. 替换为执行 wfastcgi-enable 时返回的路径
   3. `c:\users\itach\envs\trials\scripts\python.exe|c:\users\itach\envs\trials\lib\site-packages\wfastcgi.py`
2. `<add key="PYTHONPATH" value="<Path to Django App>" />`
   1. `<Path to Django App>`
   2. 替换为 Django 项目实际路径
   3. `G:\Mirror\SourceCode\trials\deploy_django`
3. `<add key="DJANGO_SETTINGS_MODULE" value="<Django App>.settings" />`
   1. `<Django App>`
   2. 替换为 Django 项目的名称
   3. `deploy_django`

则 我们得到 如下 web.config 文件


```xml
<?xml version="1.0" encoding="UTF-8"?>
    <configuration>
        <system.webServer>
            <handlers>
                <add name="Python FastCGI"
                     path="*"
                     verb="*"
                     modules="FastCgiModule"
                     scriptProcessor="c:\users\itach\envs\trials\scripts\python.exe|c:\users\itach\envs\trials\lib\site-packages\wfastcgi.py"
                     resourceType="Unspecified"
                     requireAccess="Script"/>
            </handlers>
        </system.webServer>
        <appSettings>
            <add key="WSGI_HANDLER" value="django.core.wsgi.get_wsgi_application()" />
            <add key="PYTHONPATH" value="G:\Mirror\SourceCode\trials\deploy_django" />
            <add key="DJANGO_SETTINGS_MODULE" value="deploy_django.settings" />
        </appSettings>
    </configuration>
```



## 添加静态文件虚拟目录 (未验证)
在这里插入图片描述在这里插入图片描述

添加虚拟目录时，别名与你的settings里设置的一致，比如"static"，物理路径就是静态资源的实际目录。

在 static 目录下新建一个 “web.config” 文件，然后复制下面的内容，无需修改，保存即可。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <!-- this configuration overrides the FastCGI handler to let IIS serve the static files -->
        <handlers>
            <clear/>
            <add name="StaticFile" path="*" verb="*" modules="StaticFileModule" resourceType="File" requireAccess="Read" />
        </handlers>
    </system.webServer>
</configuration>
```

至此，部署大功告成！！重启IIS，在浏览器里输入http://127.0.0.1:80，就能访问网站了,其中 端口 :80 可以省略,如果指定的是非80端口则需要显示指定





## 常见问题

### 有时候访问页面，或者单独访问网站后台出现400错误
这个时候可能是因为没有给网站权限的原因。我们打开IIS，找到网站，右键，编辑权限，给IIS用户添加修改和写入权限。就能正常访问。

时候访问页面，或者单独访问网站后台出现400错误，这个时候可能是因为没有给网站权限的原因。我们打开IIS，找到网站，右键，编辑权限，给IIS用户添加修改和写入权限。就能正常访问。



### 静态资源显示不出
在settings.py里添加STATIC_ROOT配置，指定收集静态文件路径，如：
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
进入虚拟环境，输入以下命令进行收集静态文件：
```
python manage.py collectstatic
```

如果不行的话：
在urls.py中添加：
```py
from django.contrib.staticfiles.views import serve
from django.urls import re_path

def return_static(request, path, insecure=True, **kwargs):
 return serve(request, path, insecure, **kwargs)

urlpatterns = [
 ...
 re_path(r'^static/(?P<path>.*)$', return_static, name='static'), # 添	加这行
]
```

如果还是不行：
给整个项目目录添加Everyone组和所有权限：





### HTTP 错误 500.19 - Internal Server Error
```
无法访问请求的页面，因为该页的相关配置数据无效。

详细错误信息:
模块	   IIS Web Core
通知	   未知
处理程序	   尚未确定
错误代码	   0x80070005
配置错误	   Cannot read configuration file due to insufficient permissions
配置文件	   \\?\G:\Mirror\SourceCode\trials\deploy_django\web.config
```

这种情况我们需要修改应用程序池

IIS 服务的主页, 其中有一个 `应用程序池` 的选项, 点击 `应用程序池`, 选中 `deploy_django`,左键 找到 `应用程序默认设置` 一栏, 找到 `进程模型` `标识` 选项, 将 `标识` 改为 `LocalSystem`

把 `标识` 改为 `LocalSystem`，我们再重启一下IIS中的网站，就能看到django正常运行再iis下了




### HTTP 错误 500.19 - Internal Server Error

配置错误 不能在此路径中使用此配圆节。如果在父级别上锁定了该节,便会出现这种情况。锁定是默认设的( override Mode Default="Deny"),或者是通过包舍 override Mode"Deny·或旧有的 allow Overrides" false”的位置标记明确设置的。

HTTP 错误 500.19 Internal Server Error
出现这样的情况是因为IIS7之后的版本都采用了更安全的 web.config 管理机制，默认情况下会锁住配置项不允许更改。我们把它解锁了就OK。

打开CMD，在里面依次输入下面两个命令：
```bat
C:\WINDOWS\system32>%windir%\system32\inetsrv\appcmd unlock config -section:system.webServer/handlers
Unlocked section "system.webServer/handlers" at configuration path "MACHINE/WEBROOT/APPHOST".

C:\WINDOWS\system32>%windir%\system32\inetsrv\appcmd unlock config -section:system.webServer/modules
Unlocked section "system.webServer/modules" at configuration path "MACHINE/WEBROOT/APPHOST".
```

解除了锁定之后，再访问网站就能正常显示了。



