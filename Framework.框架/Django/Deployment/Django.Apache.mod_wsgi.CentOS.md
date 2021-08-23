

## 下载与安装Apache
```sh
yum install httpd

```



## 安装mod_wsgi获取wsgi相关信息
```sh
python3 -m pip install django
python3 -m pip install mod_wsgi
```

获取 `mod_wsgi-express module-config` 配置信息，这些信息最后会在 Apache Httpd 服务中使用到。
```sh
[root@localhost python]# cd /usr/python/bin/
[root@localhost bin]# ./mod_wsgi-express module-config
LoadModule wsgi_module "/usr/python/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
WSGIPythonHome "/usr/python"
[root@localhost bin]#
```

```sh
[root@localhost html]# pwd
/var/www/html
[root@localhost html]# tree
.
└── myproject
    ├── manage.py
    └── myproject
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

2 directories, 6 files
[root@localhost html]#
```



## 部署 Django 与 Apache

打开之前的 httpd.conf 文件，在文件末尾加入以下信息

```sh
vim /etc/httpd/conf/httpd.conf
```

```conf
# 添加"mod_wsgi.so"模块，这2行都是命令"mod_wsgi-express module-config"显示出来的
LoadModule wsgi_module "/usr/python/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
WSGIPythonHome "/usr/python"


WSGIScriptAlias / /var/www/html/myproject/myproject/wsgi.py
WSGIPythonPath /var/www/html/myproject/

<Directory /var/www/html/myproject/>
   <Files wsgi.py>
      Order deny,allow
      Allow from all
   </Files>
</Directory>
```






## 访问

重启 httpd 程序
```sh
systemctl restart httpd

```


浏览器访问 127.0.0.1:80 就可以看到你的Django项目了。

浏览器中输入地址 http://127.0.0.1/admin 则可以登录 Django 的后台管理界面。

如果出错，可以进入 logs/error.conf 文件中进行查看错误信息并相应解决。






## ref
* []()
* []()
* []()
* []()
* []()

