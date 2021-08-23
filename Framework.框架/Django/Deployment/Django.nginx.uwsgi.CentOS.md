



### 配置 uwsgi

```sh
[root@localhost deploy_django]# pwd
/var/www/html/deploy_django
[root@localhost deploy_django]#

[root@localhost deploy_django]# vim uwsgi.ini
[root@localhost deploy_django]# ll
total 8
drwxr-xr-x. 4 root root 157 Apr 28 15:31 app_first
-rw-r--r--. 1 root root   0 Apr 28 15:30 db.sqlite3
drwxr-xr-x. 3 root root 108 Apr 28 15:31 deploy_django
-rw-r--r--. 1 root root 633 Apr 28 15:30 manage.py
-rw-r--r--. 1 root root 228 Apr 28 17:04 uwsgi.ini
[root@localhost deploy_django]#
[root@localhost deploy_django]# cat uwsgi.ini
[uwsgi]
socket=127.0.0.1:9090           # uwsgi 跑在哪里
master = 1                      # 
procfesses = 1                  # 
pidfile = /var/run/deploy_django.pid        # 进程的ID
daemonize = /var/log/uwsgi/deploy_django.log     # 后台运行，日志位置为 /var/log/uwsgi/deploy_django.log
module = deploy_django.wsgi:application         # 对应 Django 项目的 wsgi 配置文件路径，application 表示 wsgi 配置中生成的 APP
chdir = /var/www/html/deploy_django             # 在哪个目录下执行，也就是项目代码的路径
listen = 100

[root@localhost deploy_django]#
```

另一个 uwsgi.ini 配置示例
```ini
[uwsgi]
chdir=/root/Django/mysite/  --即网站根目录。
module=mysite.wsgi:application  --标识app位置。
static-map=/static=/root/Django/mysite/static  --表示模板引用的静态文件的目录，使用图片时必须设置。
socket=192.168.1.193:8000  --用于接收nginx请求的socket，可以是文件，而且建议是文件，这里懒的改了。
master = true   
vhost = true     
no-site = true    
workers = 2        
reload-mercy = 10    
vacuum = true       
max-requests = 1000  
limit-as = 512
buffer-size = 30000
pidfile = /var/run/uwsgi.pid
daemonize = /tmp/uwsgi.log  --uWSGI日志，安装uwsgi调试时有用。
```



## 部署 uwsgi
```sh
[root@localhost deploy_django]# mv uwsgi.ini deploy.ini
[root@localhost deploy_django]# uwsgi --ini deploy.ini
[uWSGI] getting INI configuration from deploy.ini
open("/var/log/uwsgi/deploy_django.log"): No such file or directory [core/logging.c line 288]
[root@localhost deploy_django]# mkdir -p /var/log/uwsgi/
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]# uwsgi --ini deploy.ini
[uWSGI] getting INI configuration from deploy.ini
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]# ps -ef | grep uwsgi
root     17342     1 20 17:06 ?        00:00:02 uwsgi --ini deploy.ini
root     17356 17342  0 17:06 ?        00:00:00 uwsgi --ini deploy.ini
root     17406  8292  0 17:06 pts/0    00:00:00 grep --color=auto uwsgi
[root@localhost deploy_django]# kill -HUP 17342
[root@localhost deploy_django]# ps -ef | grep uwsgi
root     17342     1  7 17:06 ?        00:00:03 /usr/local/bin/uwsgi --ini deploy.ini
root     17652  8292  0 17:06 pts/0    00:00:00 grep --color=auto uwsgi
[root@localhost deploy_django]# ps -ef | grep uwsgi
root     17342     1  8 17:06 ?        00:00:04 /usr/local/bin/uwsgi --ini deploy.ini
root     17659 17342  0 17:06 ?        00:00:00 /usr/local/bin/uwsgi --ini deploy.ini
root     17697  8292  0 17:07 pts/0    00:00:00 grep --color=auto uwsgi
[root@localhost deploy_django]#
[root@localhost deploy_django]#
```




## 代码更新后重启 uwsgi 服务器

```sh
[root@localhost nginx]# cd
[root@localhost deploy_django]# cd /var/www/html/
[root@localhost html]# cd deploy_django/
[root@localhost deploy_django]# git pull
[root@localhost deploy_django]# ps -ef | grep uwsgi
root      3692 17342  0 19:40 ?        00:00:00 /usr/local/bin/uwsgi --ini deploy.ini
root      3711  8292  0 19:41 pts/0    00:00:00 grep --color=auto uwsgi
root     17342     1  0 17:06 ?        00:00:18 /usr/local/bin/uwsgi --ini deploy.ini
[root@localhost deploy_django]#
[root@localhost deploy_django]# kill -HUP 17342
[root@localhost deploy_django]#

```


### 安装 nginx

```sh
[root@localhost deploy_django]# yum -y install nginx
[root@localhost deploy_django]# cd /etc/nginx/
[root@localhost nginx]# ll
total 68
drwxr-xr-x. 2 root root    6 Oct  8  2019 conf.d
drwxr-xr-x. 2 root root    6 Oct  8  2019 default.d
-rw-r--r--. 1 root root 1077 Oct  8  2019 fastcgi.conf
-rw-r--r--. 1 root root 1077 Oct  8  2019 fastcgi.conf.default
-rw-r--r--. 1 root root 1007 Oct  8  2019 fastcgi_params
-rw-r--r--. 1 root root 1007 Oct  8  2019 fastcgi_params.default
-rw-r--r--. 1 root root 2837 Oct  8  2019 koi-utf
-rw-r--r--. 1 root root 2223 Oct  8  2019 koi-win
-rw-r--r--. 1 root root 5170 Oct  8  2019 mime.types
-rw-r--r--. 1 root root 5170 Oct  8  2019 mime.types.default
-rw-r--r--. 1 root root 2469 Oct  8  2019 nginx.conf
-rw-r--r--. 1 root root 2656 Oct  8  2019 nginx.conf.default
-rw-r--r--. 1 root root  636 Oct  8  2019 scgi_params
-rw-r--r--. 1 root root  636 Oct  8  2019 scgi_params.default
-rw-r--r--. 1 root root  664 Oct  8  2019 uwsgi_params
-rw-r--r--. 1 root root  664 Oct  8  2019 uwsgi_params.default
-rw-r--r--. 1 root root 3610 Oct  8  2019 win-utf
[root@localhost nginx]#
```


### 配置 nginx
```sh
[root@localhost nginx]# cp nginx.conf conf.d/deploy_django.conf
[root@localhost nginx]# vim conf.d/django.conf
```
```sh
[root@localhost nginx]# cat conf.d/django.conf
server {
    listen       8000 default_server;
    listen       [::]:8000 default_server;
    server_name  localhost;
    root         /var/www/html/deploy_django;

    location / {
        uwsgi_pass 127.0.0.1:9090;
        uwsgi_param UWSGI_SCRIPT deploy_django.wsgi;
        include uwsgi_params;
    }
}

[root@localhost nginx]#
[root@localhost nginx]# nginx -s reload
```


## 访问 网页
此时，我们可以使用 服务器IP + 端口号来访问网页
```
http://192.168.123.84:8000/app_first/ok/
http://192.168.123.84:8000/admin/
```




## 添加反向代理
在 nginx.conf 也就是 nginx 的主配置文件中添加反向代理
```sh
[root@localhost nginx]# vim nginx.conf
[root@localhost nginx]# cat nginx.conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        # 反向代理 app_first 接口
        location ^~/api/ {
            proxy_pass http://127.0.0.1:8000/app_first/;

            add_header X-Slave $upstream_addr;
            proxy_redirect off;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #proxy_set_header Via "nginx";

        }

        # 反向代理 admin 接口
        location ^~/admin/ {
            proxy_pass http://127.0.0.1:8000/admin/;

            add_header X-Slave $upstream_addr;
            proxy_redirect off;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #proxy_set_header Via "nginx";
        }


        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

}

[root@localhost nginx]#
[root@localhost nginx]# nginx -s reload
```

## 访问反向代理后的网页


此时，我们可以使用 服务器IP + 端口号来访问网页
```
http://192.168.123.84:8000/app_first/ok/
http://192.168.123.84:8000/admin/

```


我们也可以使用 服务器IP + 代理接口地址  的方法访问网页
```
http://192.168.123.84/api/ok/
http://192.168.123.84/admin/
```



虽然此时在访问上有一定的优化，但是，网页上的 CSS 等效果都没有加载出来





## 静态文件


```sh
[root@localhost ~]# cd /var/www/html/deploy_django/
[root@localhost deploy_django]# ll
total 8
drwxr-xr-x. 4 root root 157 Apr 28 19:39 app_first
-rw-r--r--. 1 root root   0 Apr 28 15:30 db.sqlite3
drwxr-xr-x. 3 root root 108 Apr 29 10:50 deploy_django
-rw-r--r--. 1 root root 228 Apr 28 17:04 deploy.ini
-rw-r--r--. 1 root root 633 Apr 28 15:30 manage.py
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]#
[root@localhost deploy_django]# python3 manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
[root@localhost deploy_django]# python3 manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings.

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/usr/local/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/usr/local/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/usr/local/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/usr/local/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/usr/local/lib/python3.8/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 187, in handle
    collected = self.collect()
  File "/usr/local/lib/python3.8/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 114, in collect
    handler(path, prefixed_path, storage)
  File "/usr/local/lib/python3.8/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 338, in copy_file
    if not self.delete_file(path, prefixed_path, source_storage):
  File "/usr/local/lib/python3.8/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 248, in delete_file
    if self.storage.exists(prefixed_path):
  File "/usr/local/lib/python3.8/site-packages/django/core/files/storage.py", line 311, in exists
    return os.path.exists(self.path(name))
  File "/usr/local/lib/python3.8/site-packages/django/contrib/staticfiles/storage.py", line 38, in path
    raise ImproperlyConfigured("You're using the staticfiles app "
django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
[root@localhost deploy_django]#
```

```sh
[root@localhost deploy_django]# vim deploy_django/settings.py
[root@localhost deploy_django]# tail deploy_django/settings.py

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")          # 添加

[root@localhost deploy_django]#
```


```sh
[root@localhost deploy_django]# python3 manage.py collectstatic

128 static files copied to '/var/www/html/deploy_django/static'.
[root@localhost deploy_django]#
[root@localhost deploy_django]# ls
app_first  db.sqlite3  deploy_django  deploy.ini  manage.py  static
[root@localhost deploy_django]# ls static/
admin
[root@localhost deploy_django]# ls static/admin/
css  fonts  img  js
[root@localhost deploy_django]#
```


```sh
[root@localhost nginx]# vim conf.d/django.conf
[root@localhost nginx]#
[root@localhost nginx]#
[root@localhost nginx]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
[root@localhost nginx]# nginx -s reload
[root@localhost nginx]#
```
```sh
[root@localhost nginx]# cat conf.d/django.conf
server {
    listen       8000 default_server;
    listen       [::]:8000 default_server;
    server_name  localhost;
    root         /var/www/html/deploy_django;

    location / {
        uwsgi_pass 127.0.0.1:9090;
        uwsgi_param UWSGI_SCRIPT deploy_django.wsgi;
        include uwsgi_params;
    }

    location ^~/static {                                # 添加
        alias /var/www/html/deploy_django/static;

    }

}


[root@localhost nginx]#
```


此时，我们通过端口 `http://192.168.123.84:8000/admin/` 打开 admin 页面时，静态文件都会加载出来。

但直接通过 IP `http://192.168.123.84/admin/` 访问时,静态文件还是不能被加载出来。




## 解决通过 IP `http://192.168.123.84/admin/` 访问时不能加载 静态文件的问题

```sh
[root@localhost nginx]# vim nginx.conf
[root@localhost nginx]#
[root@localhost nginx]# nginx -s reload
[root@localhost nginx]#
```

```sh
[root@localhost nginx]# cat nginx.conf
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;


        location ^~/api/ {
            proxy_pass http://127.0.0.1:8000/app_first/;

            add_header X-Slave $upstream_addr;
            proxy_redirect off;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #proxy_set_header Via "nginx";

        }


        location ^~/admin/ {
            proxy_pass http://127.0.0.1:8000/admin/;

            add_header X-Slave $upstream_addr;
            proxy_redirect off;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #proxy_set_header Via "nginx";
        }


        location ^~/static {                                # 添加
            alias /var/www/html/deploy_django/static;

         }



        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

}

[root@localhost nginx]#

```


