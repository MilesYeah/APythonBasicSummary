# python中给程序加锁之fcntl模块的使用

python 中给文件加锁——fcntl模块


This works only on Unix systems.




fcntl模块：
* flock() : flock(f, operation)

operation : 包括：
* fcntl.LOCK_UN 解锁
* fcntl.LOCK_EX  排他锁
* fcntl.LOCK_SH  共享锁
* fcntl.LOCK_NB  非阻塞锁
* LOCK_SH 共享锁:所有进程没有写访问权限，即使是加锁进程也没有。所有进程有读访问权限。
* LOCK_EX 排他锁:除加锁进程外其他进程没有对已加锁文件读写访问权限。
* LOCK_NB 非阻塞锁: 如果指定此参数，函数不能获得文件锁就立即返回，否则，函数会等待获得文件锁。
* LOCK_NB可以同LOCK_SH或LOCK_NB进行按位或（|）运算操作。 fcnt.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)

## 示例
```py
import fcntl

# 打开一个文件
# 当前目录下test文件要先存在，如果不存在会报错。或者以写的方式打开
f = open('./test')
# 对该文件加密：
fcntl.flock(f,fcntl.LOCK_EX)
# 这样就对文件test加锁了，如果有其他进程对test文件加锁，则不能成功，会被阻塞，但不会退出程序。
#解锁：
fcntl.flock(f,fcntl.LOCK_UN)
```

```py
import sys
import time
import fcntl

class FLOCK(object):

    def __init__(self, name):
        self.fobj = open(name, 'w')
        self.fd = self.fobj.fileno()

    def lock(self):
        try:
            fcntl.lockf(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  # 给文件加锁，使用了fcntl.LOCK_NB
            print('给文件加锁，稍等 ... ...')
            time.sleep(20)
            return True
        except:
            print('文件加锁，无法执行，请稍后运行。')
            return False


def unlock(self):
    self.fobj.close()
    print('已解锁')

if __name__ == "__main__":
    print(sys.argv[1])
    locker = FLOCK(sys.argv[1])
    a = locker.lock()
    if a:
        print('文件已加锁')
    else:
        print('无法执行，程序已锁定，请稍等')
```


先运行一个终端会打印：
```
python lockfile.py test

test

给文件加锁，稍等 ... ...

文件已加锁
```

运行另外一个终端：
```
test

文件加锁，无法执行，请稍后运行。

无法执行，程序已锁定，请稍等
```

