# Python socket imooc

## Socket简介
socket 是什么
* socket是电脑网络中进程间的数据流的端点。
* socket是操作系统的通信机制
* 应用程序通过socket进行网络数据传输

## TCP通信过程


## socket通信过程



## socket 通信方式
* TCP
  * 在通信之前需要client与server连接
  * 同一时间只能有一个client与server相连，当多个client相连的时候直接是阻塞状态
  * socket.listen(5)指的是最大监听5个链接，但是并不是说可以同时有五个连接能够连上server。
    * 当有多个连接时，除了第一个连接是连上server的之外，其余链接都处于阻塞状态。
    * 当有超过5个链接时，这些超出的链接会直接被server拒绝。
  * 需要显示的关闭连接
* UDP
  * 在通信之前不需要client与server连接
  * 同时可以有多个client与server相连
  * 不需要显示的关闭连接，但是为了更好的利用资源还是建议在程序最后显示加入链接的关闭


## 为什么是socket
* socket能够适应多种网络协议
* socket是基础应用，了解socket能够举一反三
* 服务器传输中涉及到大量网络协议，离不开socket应用



## Socket参数

实例化一个socket对象
```py
import socket
sk = socket.socket()
```

一共分为三个：
* family: 地址簇
    * socket.AF_INET    IPv4（默认）
    * socket.AF_INET6   IPv6
    * socket.AF_UNIX    只能用于单一的Unix系统进程间的通信
* type: 类型
    * socket.SOCK_STREAM    流式socker， for TCP（默认）
    * socket.SOCK_DGRAM     数据报式socket, for UDP
    * socket.SOCK_RAW       原始套接字（使用的较少）
    * socket.SOCK_RDM       可靠UDP形式（较少，加上了校验）
    * socket.SOCK_SEQPACKET 可靠的连续数据包服务（较少）
* proto：协议号
    * 0： 默认，可以省略
    * CAN_RAW或CAN_BCM：地址簇为AF_CAN时



## socket 的非阻塞实现
使用 `socketserver`，
socketserver在定义的过程中导入了threading模块，其原理就是使用多线程的方式来实现非阻塞。
每当有一个链接过来时，socketserver就会开启一个新的线程。

### 