# Python threading condition

Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

可以把Condiftion理解为一把高级的琐，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。threadiong.Condition在内部维护一个琐对象（默认是RLock），可以在创建Condigtion对象的时候把琐对象作为参数传入。

Condition也提供了acquire, release方法，其含义与琐的acquire, release方法一致，其实它只是简单的调用内部琐对象的对应的方法而已。



### 构造方法： 
Condition([lock/rlock])



### 实例方法： 
* acquire([timeout])/release(): 调用关联的锁的相应方法。 
* wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。 
* notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。 
* notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。





### 示例代码

#### 例子一：生产者消费者模型

```python
# encoding: UTF-8
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()


# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print('produce...')
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print('consume...')
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()

```

运行结果
```python
produce...
consume...
produce...
consume...
produce...
consume...
produce...
consume...
produce...
consume...

Process finished with exit code -1
程序不断循环运行下去。重复生产消费过程。

```

#### 例子二：生产者消费者模型 使用类改造
```python
import threading
import time

condition = threading.Condition()
products = 0


class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1
                    print(f"Producer({self.name}):deliver one, now products:{products}")
                    condition.notify()  #不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print(f"Producer({self.name}):already 10, stop deliver, now products:{products}")
                    condition.wait()    #自动释放锁定
                time.sleep(2)


class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print(f"Consumer({self.name}):consume one, now products:{products}")
                    condition.notify()
                    condition.release()
                else:
                    print(f"Consumer({self.name}):only 1, stop consume, products:{products}")
                    condition.wait()
                time.sleep(2)


if __name__ == "__main__":
    for p in range(0, 2):
        prod = Producer(name=f"producer_{p}")
        # prod = Producer()
        prod.start()

    for c in range(0, 3):
        cons = Consumer(name=f"consumer_{c}")
        # cons = Consumer()
        cons.start()

```

```
C:\Users\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tThreadProcess/threadCondition/producerConsumer2.py
Producer(producer_0):deliver one, now products:1
Producer(producer_1):deliver one, now products:2
Consumer(consumer_0):consume one, now products:1
Consumer(consumer_1):only 1, stop consume, products:1
Consumer(consumer_2):only 1, stop consume, products:1
Consumer(consumer_0):only 1, stop consume, products:1
Producer(producer_1):deliver one, now products:2
Producer(producer_0):deliver one, now products:3
Consumer(consumer_1):consume one, now products:2
Consumer(consumer_1):consume one, now products:1
Consumer(consumer_1):only 1, stop consume, products:1
Consumer(consumer_2):only 1, stop consume, products:1
Producer(producer_1):deliver one, now products:2
Producer(producer_0):deliver one, now products:3
Consumer(consumer_0):consume one, now products:2
Consumer(consumer_0):consume one, now products:1
Consumer(consumer_0):only 1, stop consume, products:1
Consumer(consumer_1):only 1, stop consume, products:1
Consumer(consumer_2):only 1, stop consume, products:1
Producer(producer_1):deliver one, now products:2
Producer(producer_0):deliver one, now products:3
Consumer(consumer_0):consume one, now products:2
Consumer(consumer_0):consume one, now products:1
Consumer(consumer_0):only 1, stop consume, products:1
Consumer(consumer_1):only 1, stop consume, products:1
Producer(producer_1):deliver one, now products:2
Producer(producer_0):deliver one, now products:3

Process finished with exit code -1

```



#### 例子三：
```python
import threading

alist = None
condition = threading.Condition()


def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()


def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print(i, )
        condition.release()


def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notify_all()
        condition.release()


tset = threading.Thread(target=doSet, name='tset')
tprint = threading.Thread(target=doPrint, name='tprint')
tcreate = threading.Thread(target=doCreate, name='tcreate')
tset.start()
tprint.start()
tcreate.start()

```

```
C:\Users\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tThreadProcess/threadCondition/producerConsumer3.py
0
0
0
0
0
0
0
0
0
0

Process finished with exit code 0
```
