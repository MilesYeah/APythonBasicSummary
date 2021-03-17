# 替换OS中原有的Python2成为python3

```sh
[root@localhost Python-3.8.8]# whereis python3
python3: /usr/local/bin/python3.8 /usr/local/bin/python3.8-config /usr/local/bin/python3 /usr/local/lib/python3.8
[root@localhost Python-3.8.8]# cd /usr/local/bin/
[root@localhost bin]# ls
2to3  2to3-3.8  easy_install-3.8  idle3  idle3.8  pip3  pip3.8  pydoc3  pydoc3.8  python3  python3.8  python3.8-config  python3-config
[root@localhost bin]# whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/local/bin/python3.8 /usr/local/bin/python3.8-config /usr/local/lib/python3.8 /usr/include/python2.7 /usr/share/man/man1/python.1.gz
[root@localhost bin]#
```

```sh
[root@localhost bin]# cd /usr/bin/
[root@localhost bin]# mv python python.bak
# 注意是添加软链接
[root@localhost bin]# ln -s /usr/local/bin/python3 /usr/bin/python
```





## 替换后导致yum出现的问题


```sh
[root@localhost bin]# yum
  File "/usr/bin/yum", line 30
    except KeyboardInterrupt, e:
                            ^
SyntaxError: invalid syntax
[root@localhost bin]#
```

```sh
[root@localhost bin]# whereis yum
yum: /usr/bin/yum /etc/yum.conf /etc/yum /usr/share/man/man8/yum.8
[root@localhost bin]# vim yum
[root@localhost bin]#
```
编辑yum我们就会发现，其实yum是一个脚本
由于yum的默认解释器是 python2，默认的python命令我们换成了python3环境，所以导致yum脚本不能使用。

所以需要将yum脚本的解释器替换成python2。
```sh
#!/usr/bin/python2
import sys
try:
    import yum
except ImportError:
    print >> sys.stderr, """\
There was a problem importing one of the Python modules
required to run yum. The error leading to this problem was:

   %s
```

