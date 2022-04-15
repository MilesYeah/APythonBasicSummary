
Python—实现ssh客户端（连接远程服务器）


paramiko 是一个基于SSH用于连接远程服务器并执行相关操作（SSHClient和SFTPClinet，即一个是远程连接，一个是上传下载服务），使用该模块可以对远程服务器进行命令或文件操作，值得一说的是，fabric和ansible内部的远程管理就是使用的paramiko来实现的。

Paramiko 模块是基于Python实现的SSH远程安全连接，用于SSH远程执行命令、文件传输等功能。

默认Python没有自带，需要手动安装：`pip install paramiko`。
如果安装失败，可以尝试yum安装：`yum install python-paramiko`。

除了Paramiko模块，还有相同作用的fabric和pexpect模块。


## SSH客户端实现方案一，远程执行命令（密码认证）

```py
# -*- coding:utf-8 -*-
import paramiko  # 先安装pycrypto，再安装paramiko
 
# 创建SSH对象
ssh = paramiko.SSHClient()
 
# 允许连接不在~/.ssh/known_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# 连接服务器
ssh.connect(hostname="106.15.88.182", port=22, username="root", password="123456")
 
# 执行命令，不要执行top之类的在不停的刷新的命令(可以执行多条命令，以分号来分隔多条命令)
# stdin, stdout, stderr = ssh.exec_command("cd %s;mkdir %s" % ("/www/wwwroot", "aa"))
stdin, stdout, stderr = ssh.exec_command("python /www/wwwroot/test.py")
stdin.write("终端等待输入...\n")   # test.py文件有input()函数，如果不需要与终端交互，则不写这两行
stdin.flush()
 
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
res = result.decode()
res = result.decode("utf-8")
res = result.decode(encoding="utf-8")
print res
 
# 关闭服务器连接
ssh.close()
```





## SSH客户端实现方案二，远程执行命令（密码认证）


```py
import paramiko
 
transport = paramiko.Transport(("106.15.88.182", 22))
transport.connect(username="root", password="123456")              # 建立连接
# transport.connect(username="root", password="口令", hostkey="密钥")
 
# 创建SSH对象,SSHClient是定义怎么传输命令、怎么交互文件
ssh = paramiko.SSHClient()
ssh._transport = transport
 
# 执行命令，不要执行top之类的在不停的刷新的命令
stdin, stdout, stderr = ssh.exec_command("df")
 
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
print result.decode()
 
# 关闭服务器连接
transport.close()
```


## SSH客户端实现方案三，远程执行命令（密码认证）


```py
import paramiko
 
client = paramiko.SSHClient()   # 创建SSH对象
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())# 允许连接不在known_hosts文件中的主机
 
# 连接服务器,以用户名和密码进行认证
client.connect(hostname="106.15.88.182", port=22, username="root", password="123456")
 
#实例化Transport，并建立会话Session
ssh_session = client.get_transport().open_session()
if ssh_session.active:
    ssh_session.exec_command("df")
    print ssh_session.recv(1024)
 
# 关闭服务器连接
client.close()
```

## SSH客户端实现方案四，远程执行命令（密钥认证）


```py
import paramiko
 
ssh = paramiko.SSHClient()     # 创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
 
#这里写我们的密钥文件
private_key = paramiko.RSAKey.from_private_key_file("key.poem")
# 连接服务器，这里我们用pkey参数设置为私钥登陆
ssh.connect(hostname="106.15.88.182", port=22, username="root", pkey=private_key)
 
stdin, stdout, stderr = ssh.exec_command('df')   # 执行命令
res, err = stdout.read(), stderr.read()          # stdout.readline()
result = res if res else err
print result.decode()
 
ssh.close()   # 关闭连接
```


## 封装之后的使用

```py
import sys,logging
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import AuthenticationException
from paramiko.ssh_exception import NoValidConnectionsError
 
class SshClient():
    def __init__(self):
        self.ssh_client = SSHClient()
 
    def ssh_login(self, host_ip, username, password):
        try:
            # 设置允许连接known_hosts文件中的主机（默认连接不在known_hosts文件中的主机会拒绝连接抛出SSHException）
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(host_ip, port=22, username=username, password=password)
        except AuthenticationException:
            logging.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            logging.warning('connect time out')
            return 1002
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return 1003
        return 1000
 
    def execute_some_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        print stdout.read().decode()
 
    def ssh_logout(self):
        self.ssh_client.close()
 
if __name__ == "__main__":
    command = "whoami"       # 自己使用ssh时，命令怎么敲的command参数就怎么写
    ssh = SshClient()
    if ssh.ssh_login(host_ip="106.15.88.188", username="root", password="abc0506") == 1000:
        ssh.execute_some_command(command)
        ssh.ssh_logout()
```


## ref
https://www.cnblogs.com/breezey/p/6663546.html

https://blog.csdn.net/cc297322716/article/details/78608283

https://www.jb51.net/article/125681.htm

