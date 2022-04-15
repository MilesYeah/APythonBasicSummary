


## 下载与安装Apache



选择对应电脑版本下载Apache2.4：[下载地址](https://www.apachelounge.com/download/)

我的是64位win7，所以下载的是第一个。

下载完成之后解压到文件夹，进入文件夹的 `C:\ProgramsMine\ApacheLounge\Apache24` 目录下。

```bat
C:\Users\Itach>cd \ProgramsMine\ApacheLounge\Apache24

C:\ProgramsMine\ApacheLounge\Apache24>dir
 Volume in drive C is OS.1.9T.0
 Volume Serial Number is 72AD-8ECA

 Directory of C:\ProgramsMine\ApacheLounge\Apache24

2021/04/29  16:51    <DIR>          .
2021/04/29  16:51    <DIR>          ..
2020/02/21  08:33            13,741 ABOUT_APACHE.txt
2021/04/29  16:32    <DIR>          bin
2021/04/29  16:32    <DIR>          cgi-bin
2021/03/27  18:12                61 CHANGES.txt
2021/04/29  16:32    <DIR>          conf
2021/04/29  16:32    <DIR>          error
2021/04/29  16:32    <DIR>          htdocs
2021/04/29  16:32    <DIR>          icons
2021/04/29  16:32    <DIR>          include
2016/05/18  01:59             3,869 INSTALL.txt
2021/04/29  16:32    <DIR>          lib
2021/03/27  18:17            44,494 LICENSE.txt
2021/04/29  16:40    <DIR>          logs
2021/04/29  16:32    <DIR>          manual
2021/04/29  16:32    <DIR>          modules
2021/04/29  16:49           363,900 mod_wsgi-4.7.1-cp39-cp39-win32.whl
2021/04/29  16:50           372,185 mod_wsgi-4.7.1-cp39-cp39-win_amd64.whl
2021/03/27  18:13             2,865 NOTICE.txt
2021/03/27  18:32            44,907 OPENSSL-NEWS.txt
2021/03/27  18:32             4,545 OPENSSL-README.txt
2014/01/24  00:33             4,752 README.txt
              10 File(s)        855,319 bytes
              13 Dir(s)  49,510,027,264 bytes free

C:\ProgramsMine\ApacheLounge\Apache24>
```


## 配置Apache
打开 conf/httpd.conf 文件，进行一些修改。

```
# 直接定义 SRVROOT ,如下的全都是用这个变量替代了,所以其他的直接引用 SRVROOT 即可,不用修改
#Define SRVROOT "c:/Apache24"
Define SRVROOT "C:\ProgramsMine\ApacheLounge\Apache24"

# Listen 80
Listen 127.0.0.1:8080

#ServerName www.example.com:80
ServerName 127.0.0.1:8080

```



## 安装mod_wsgi获取wsgi相关信息

使用 `pip install mod_wsgi` 安装，

如果提示如下错误，则需要安装 Build Tools
```
    running build_ext
    building 'mod_wsgi.server.mod_wsgi' extension
    error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/
```    

下载 [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/) 下载 `Build Tools for Visual Studio 2019` / `Visual Studio 2019 生成工具`



安装完成后，获取 mod_wsgi 配置信息。
```
mod_wsgi-express module-config
```
将显示出来的三条信息记住，后面配置文件中要用到。

```bat
C:\ProgramsMine\ApacheLounge\Apache24>mod_wsgi-express module-config
LoadFile "c:/python390/python39.dll"
LoadModule wsgi_module "c:/python390/lib/site-packages/mod_wsgi/server/mod_wsgi.cp39-win_amd64.pyd"
WSGIPythonHome "c:/python390"
C:\ProgramsMine\ApacheLounge\Apache24>
```






## 部署 Django 与 Apache

打开之前的 httpd.conf 文件，在文件末尾加入以下信息

```conf
# 添加"mod_wsgi.so"模块，这三行都是命令"mod_wsgi-express module-config"显示出来的
LoadFile "c:/python390/python39.dll"
LoadModule wsgi_module "c:/python390/lib/site-packages/mod_wsgi/server/mod_wsgi.cp39-win_amd64.pyd"
WSGIPythonHome "c:/python390"
```


Django 项目的路径配置
```conf

# 项目存放的上级名称
Define DjangoBase "G:/Mirror/SourceCode/trials"
# 项目名称
Define DjangoProj "deploy_django"
# 拼接成 Django 项目根目录
Define DjangoRoot "${DjangoBase}/${DjangoProj}"

# 指定项目的"wsgi.py"配置文件路径
WSGIScriptAlias / "${DjangoRoot}/${DjangoProj}/wsgi.py"

# 指定Django项目根目录，并配置访问权限。WSGIPythonPath取代DocumentRoot配置，或者保留DocumentRoot一致
WSGIPythonPath "${DjangoRoot}"
<Directory "${DjangoRoot}">
    Require all granted
</Directory>

# 项目静态文件配置 
Alias /static "${DjangoRoot}/static"
<Directory "${DjangoRoot}/static">
    AllowOverride None
    Options None
    Require all granted
</Directory>

# 项目media文件配置, 用户上传图片等媒体文件
Alias /media "${DjangoRoot}/media"
<Directory "${DjangoRoot}/media">
    AllowOverride None  
    Options None  
    Require all granted  
</Directory>

```



## 访问

重启httpd.exe程序，浏览器访问 127.0.0.1:8080 就可以看到你的Django项目了。

如果出错，可以进入 logs/error.conf 文件中进行查看错误信息并相应解决。

成功部署后如果想要你的Django项目能通过局域网访问，则需要进一步的配置。

进入 httpd.conf 文件中，修改前面设置的Listen和ServerName为

Listen 你的IP地址:80  
......  
ServerName 你的IP地址:80  
如果不知道自己的ip地址

参考： 点击打开链接

保存文件，然后重启httpd.exe程序就OK了。





## ref
* [原文链接：](https://blog.csdn.net/Mr_blueD/article/details/79759483)
* []()
* []()
* []()
* []()
* []()















# Linux 




[root@localhost conf]# mod_wsgi-express module-config
LoadModule wsgi_module "/usr/local/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
WSGIPythonHome "/usr/local"
[root@localhost conf]#










