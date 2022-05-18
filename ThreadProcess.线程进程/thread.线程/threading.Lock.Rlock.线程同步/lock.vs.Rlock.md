# Python threading lock/rlock

由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。

## Lock
Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

## Rlock
RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

简言之：`Lock属于全局，Rlock属于线程。`


## 实例方法： 
* acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。 
* release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

### 例子一（未使用锁）
```python
#coding:utf-8
import threading
import time

gl_num = 0

def show(arg):
    global gl_num
    time.sleep(1)
    gl_num +=1
    print(gl_num)

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')
```
未使用锁

运行结果
```
C:\Users\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tThreadProcess/tThreadLock/0.noLock.py
main thread stop
123
4567

8



910



Process finished with exit code 0

```

多次运行可能产生混乱。这种场景就是适合使用锁的场景。

### 例子二（使用锁） (sleep 放在lock内)

```python
import threading
import time

gl_num = 0

lock = threading.RLock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()

```
使用Lock

运行结果
```
C:\Users\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tThreadProcess/tThreadLock/0.hasLock.py
1
2
3
4
5
6
7
8
9
10

Process finished with exit code 0

```
可以看出，全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性

### 例子二（使用锁） (sleep 放在lock外)

```py
import threading
import time

gl_num = 0

lock = threading.RLock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    time.sleep(1)
    lock.acquire()
    global gl_num
    gl_num += 1
    print(gl_num)
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()

```
```
C:\Users\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tThreadProcess/tThreadLock/0.hasLock.2.py
1
2
3
4
5
6
7
8
9
10

Process finished with exit code 0
```
可以看到结果一下子全都出来，而上述将sleep放在锁内的则是需要约10秒才能结束程序


## Lock对比Rlock
这两种琐的主要区别是：
* RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
* 注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。

```python
#coding:utf-8
 
import threading
lock = threading.Lock() #Lock对象
lock.acquire()
lock.acquire()  #产生了死锁。程序将会在此卡死
lock.release()
lock.release()
print(lock.acquire())
``` 
 
```python
import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire() #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()
```

