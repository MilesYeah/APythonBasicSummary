# [python3 nmap 函数简介](https://blog.csdn.net/whatday/article/details/103601133)

whatday 2019-12-18 18:26:06  921  收藏
版权
简介

python-nmap是一个使用nmap进行端口扫描的python库，它可以很轻易的生成nmap扫描报告，并且可以帮助系统管理员进行自动化扫描任务和生成报告。同时，它也支持nmap脚本输出。

可以看到python-nmap只有四个py文件(__init__.py, nmap.py, test.py, test_nmap.py)，下面就一一进行解读



 

## __init__.py
 除去几十行的注释外，真正的代码只有四行，基本内容就是从同目录的nmap.py下导入一些基本信息：作者(__author__)，版本(__version__)，最后修改日期(__last_modification__)，这些在nmap.py下都有写





 

## test.py
 test.py也只有简单的几行，运行时就是打印出本地的Host，猜测是用来测试是否可以利用nmap的扫描功能 



 

## nmap.py
nmap.py用于调用nmap的功能进行扫描，主要的扫描函数为PortScanner(object):

 

### class PortScanner(object):

PortScanner类的英文注释就写着功能：PortScanner class allows to use nmap from python（PortScanner类允许在python使用nmap）

#### def __init__(self, nmap_search_path=('nmap', '/usr/bin/nmap', '/usr/local/bin/nmap', '/sw/bin/nmap', '/opt/local/bin/nmap')):
主要功能就是在nmap_search_path查找nmap的路径（从nmap_search_path可以看出在Windows下使用得自己添加路径）和初始化PortScanner模块，包括本机上nmap的路径(self._nmap_path)，扫描的结果(self._scan_result)，nmap的主版本(self._nmap_version_number),  nmap的子版本(self._nmap_subversion_number),  nmap输出的版本信息(self._nmap_last_output)，是否找到nmap(is_nmap_found)



#### def get_nmap_last_output(self):
返回文本输出，可能用于调试，这里有作者的英文注释

 

#### def nmap_version(self):
如果检查到nmap返回nmap的版本信息

 

#### def listscan(self, hosts='127.0.0.1'):
不进行扫描，但解析目标主机并返回一个主机列表



 

#### def scan(self, hosts='127.0.0.1', ports=None, arguments='-sV', sudo=False):
调用nmap的扫描功能进行扫描，以json格式输出

 

 

#### def analyse_nmap_xml_scan(self, nmap_xml_output=None, nmap_err='', nmap_err_keep_trace='', nmap_warn_keep_trace=''):
对nmap的扫描结果进行处理，扫描结果是XML形式，转化为json形式打印出来

 

#### def __getitem__(self, host):
返回目标ip

 

#### def all_hosts(self):
以列表形式返回目标ip

 

#### def command_line(self):
返回输入的命令行

 

#### def scaninfo(self):
以结构体形式返回扫描信息

 

#### def scanstats(self):
以结构体形式返回扫描状态

 

#### def has_host(self, host):
如果目标主机有回应就返回True（检查是否有目标主机）

 

#### def csv(self):
把csv输出转化为文本返回

 

#### def __scan_progressive__(self, hosts, ports, arguments, callback, sudo):
用于PortScannerAsync的回调

 

### class PortScannerAsync(object):

允许异步使用python中的nmap，每个主机的扫描结果都会通过回调返回，进行多线程扫描

#### def __init__(self):
调用PortScanner()检查nmap所在的系统和和nmap版本

 

#### def __del__(self):
用于对self._process清零，self._process用来存放扫描信息

 

#### def scan(self, hosts='127.0.0.1', ports=None, arguments='-sV', callback=None, sudo=False):
调用多线程扫描，并且结果通过回调函数返回

 

#### def stop(self):
 停止当前的扫描过程

 

#### def wait(self, timeout=None):
等待当前扫描进程的结束和超时

 

#### def still_scanning(self):
检查当前进程是否还在扫描

 

### class PortScannerYield(PortScannerAsync):

针对主机的扫描结果调用Yield进行处理

#### def __init__(self):
调用PortScanner()检查nmap所在的系统和和nmap版本

 

#### def scan(self, hosts='127.0.0.1', ports=None, arguments='-sV', sudo=False):
把扫描结果放到迭代器里进行回调

 

### class PortScannerHostDict(dict):

PortScannerHostDict：用于存储和访问主机扫描结果的字典类

#### def hostnames(self):
以列表形式返回主机名

 #### def hostname(self):
返回第一个主机名，为了兼容性问题，不甚理解

#### def state(self):
#### def uptime(self):
 两个都是返回主机的状态信息

#### def all_protocols(self):
 all_protocols：以列表形式返回扫描的协议

#### def all_tcp(self):
#### def has_tcp(self, port):
#### def tcp(self, port):
 三个函数的作用就是列出扫描到的TCP端口的信息

#### def all_udp(self):
#### def has_udp(self, port):
#### def udp(self, port):
 三个函数的作用就是列出扫描到的UDP端口的信息

#### def all_ip(self):
#### def has_ip(self, port):
#### def ip(self, port):
 三个函数的作用就是列出扫描到的IP端口的信息

#### def all_sctp(self):
#### def has_sctp(self, port):
#### def sctp(self, port):
 三个函数的作用就是列出扫描到的SCTP端口的信息

 

### class PortScannerError(Exception):

为PortScanner检测异常的类

返回异常信息



 #### def __get_last_online_version():
 通过查询官网获得最新的python-nmap的版本信息，如0.6.1

 

 #### def convert_nmap_output_to_encoding(value, code="ascii"):
 对Unicode编码的scan_result对象进行编码的转换，作为字典返回

 

## test_nmap.py
 test_nmap.py是用来对python-nmap进行测试和对nmap是否正常运行的检查，无论是pdb库还是nose测试框架都经常用于python的测试和调试

 

### class Pdb(Plugin):

提供调试选项，如果在程序测试时遇到错误或故障会放到pdb里进行调试

#### def options(self, parser, env):
 定义命令行选项：包括--pdb, --pdb-failures,  --pdb-errors

 

#### def configure(self, options, conf):
 通过检查异常来匹配哪一个类型的异常触发插件

 

#### def addError(self, test, err):
 如果配置调试结果是调试错误把错误放入pdb

 

#### def addFailure(self, test, err):
 如果配置调试结果是调试失败把错误放入pdb

 

#### def debug(self, err):
 不甚理解，猜测是输出错误信息

 

#### def setup_module():
 设置扫描模块进行扫描

 

#### def test_wrong_args():
 测试输入的错误参数

 

#### def test_host_scan_error():
 测试主机扫描的错误

 

#### def xmlfile_read_setup():
 测试是否能读取xml文件

 

#### def test_command_line():
 测试输入命令行的命令是否合法

 

#### def test_scan_info():
 测试扫描信息是否存在

 

#### def test_all_hosts():
#### def test_host():
#### def test_host_no_hostname():
#### def test_port():
 45.33.32.156是nmap的官网里的一个机器人，用来测试nmap是否能正确的运行

 

#### def test_listscan():
测试列表扫描主机的结果

 

#### def test_csv_output():
 测试输出格式是否为CSV

 

#### def test_listscan():
 测试列表扫描

 

#### def test_ipv6():
 测试对IPV6的扫描

 

#### def test_ipv4_async():
 测试IPV4的异步扫描

 

#### def test_ipv6_async():
 测试IPV6的异步扫描

 

#### def scan_localhost_sudo_arg_O():
 扫描本地主机用户的信息

 

#### def test_sudo():
 测试主机信息

 

#### def test_parsing_osmap_osclass_and_others():
 测试是否获得主机的信息

 

#### def test_all_protocols():
 测试本地主机的信息

 

#### def xmlfile_read_setup_multiple_osmatch():
 读取osmatch_output.xml文件，设置osmatch的xml格式输出

 

#### def test_multipe_osmatch():
 检查主机的osmatch里是否存在一些信息

 

#### def test_convert_nmap_output_to_encoding():
 测试是否对nmap扫描结果进行了编码

 

#### def test_WARNING_case_sensitive():
 测试warning的警告信息是否存在

 

#### def test_scan_progressive():
 测试异步扫描的情况

