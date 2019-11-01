# python select模块


## select介绍
select()的机制中提供一fd_set的数据结构，实际上是一long类型的数组， 每一个数组元素都能与一打开的文件句柄（不管是Socket句柄，还是其他文件或命名管道或设备句柄）建立联系，建立联系的工作由程序员完成， 当调用select()时，由内核根据IO状态修改fd_set的内容，由此来通知执行了select()的进程哪一Socket或文件可读或可写。主要用于Socket通信当中。

总结：select主要用于socket通信当中，能监视我们需要的文件描述变化。



 
## 非阻塞式I/O编程特点
* 如果一个发现I/O有输入，读取的过程中，另外一个也有了输入，这时候不会产生任何反应.这就需要你的程序语句去用到select函数的时候才知道有数据输入。
* 程序去select的时候，如果没有数据输入，程序会一直等待，直到有数据为止，也就是程序中无需循环和sleep。

Select在Socket编程中还是比较重要的，可是对于初学Socket的人来说都不太爱用Select写程序，他们只是习惯写诸如connect、accept、recv或recvfrom这样的阻塞程序（所谓阻塞方式block，顾名思义，就是进程或是线程执行到这些函数时必须等待某个事件的发生，如果事件没有发生，进程或线程就被阻塞，函数不能立即返回）。

可是使用Select就可以完成非阻塞（所谓非阻塞方式non-block，就是进程或线程执行此函数时不必非要等待事件的发生，一旦执行肯定返回，以返回值的不同来反映函数的执行情况，如果事件发生则与阻塞方式相同，若事件没有发生，则返回一个代码来告知事件未发生，而进程或线程继续执行，所以效率较高）方式工作的程序，它能够监视我们需要监视的文件描述符的变化情况——读写或是异常。

返回值：准备就绪的描述符数，若超时则返回0，若出错则返回-1。


 

## 示例

### 示例1：模拟select，同时监听多个端口
服务端s1.py
```py
import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8001))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('0.0.0.0', 8002))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('0.0.0.0', 8003))
sk3.listen()

inputs = [sk1, sk2, sk3, ]

while True:
    r_list, w_list, e_list = select.select(inputs,[],inputs,1)
    for sk in r_list:
        # conn表示每一个连接对象
        conn, address = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()

    for sk in e_list:
        inputs.remove(sk)
```

解释：
* select内部自动监听sk1,sk2,sk3三个对象，监听三个句柄是否发生变化，把发生变化的元素放入r_list中。
* 如果有人连接sk1，则r_list = [sk1]
* 如果有人连接sk1和sk2，则r_list = [sk1,sk2]
* select中第1个参数表示inputs中发生变化的句柄放入r_list。
* select中第2个参数表示[]中的值原封不动的传递给w_list。
* select中第3个参数表示inputs中发生错误的句柄放入e_list。
* 参数1表示1秒监听一次
* 当有用户连接时，r_list里面的内容[<socket.socket fd=220, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 8001)>]




客户端c1.py
```py
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

content = str(obj.recv(1024), encoding='utf-8')
print(content)

obj.close()
```

客户端c2.py
```py
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8002))

content = str(obj.recv(1024), encoding='utf-8')
print(content)

obj.close()
```




### 示例2：IO多路复用--使用socket模拟多线程，并实现读写分离
服务端s1.py
```py
#使用socket模拟多线程，使多用户可以同时连接
import socket
import select

sk1 = socket.socket()
sk1.bind(('0.0.0.0', 8001))
sk1.listen()

inputs = [sk1, ]
outputs = []
message_dict = {}

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
    print('正在监听的socket对象%d' % len(inputs))
    print(r_list)
    for sk1_or_conn in r_list:
        #每一个连接对象
        if sk1_or_conn == sk1:
            # 表示有新用户来连接
            conn, address = sk1_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []
        else:
            # 有老用户发消息了
            try:
                data_bytes = sk1_or_conn.recv(1024)
            except Exception as ex:
                # 如果用户终止连接
                inputs.remove(sk1_or_conn)
            else:
                data_str = str(data_bytes, encoding='utf-8')
                message_dict[sk1_or_conn].append(data_str)
                outputs.append(sk1_or_conn)

    #w_list中仅仅保存了谁给我发过消息
    for conn in w_list:
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str+'好', encoding='utf-8'))
        outputs.remove(conn)

    for sk in e_list:

        inputs.remove(sk)
```

客户端c1.py
```py
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = input('>>>')
    obj.sendall(bytes(inp, encoding='utf-8'))
    ret = str(obj.recv(1024),encoding='utf-8')
    print(ret)

obj.close()
```
