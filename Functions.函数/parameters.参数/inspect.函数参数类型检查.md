# 函数参数类型检查
思路：

函数参数的检查，一定是在函数外
函数应该作为参数，传入到检查函数中
检查函数拿到函数传入的实际参数，与形参声明对比
__annotations__属性是一个字典，其中包括返回值类型的声明，假设要做一个位置参数的判断，无法和字典中的声明对应，使用inspect模块


## inspect模块
提供获取对象信息的函数，可以检查函数和类、类型检查
inspect模块
signature(callable)，获取签名（函数签名包含一个函数的信息，包括函数名、它的参数类型、它所在的类和名称空间及其他信息）

```py
import inspect

def add(x:int,y:int,*args,**kwargs)->int:
    return x+y

sig =  inspect.signature(add)
print("sig,type(sig): ", sig,type(sig)) #获取签名
print('params : ',sig.parameters) #OrderedDict
print('return : ',sig.return_annotation) #返回值类型
print("sig.parameters['y']: ", sig.parameters['y'], type(sig.parameters['y']))
print("sig.parameters['x']: ", sig.parameters['x'].annotation)
print("sig.parameters['args']: ", sig.parameters['args'])
print("sig.parameters['args']: ", sig.parameters['args'].annotation)
print("sig.parameters['kwargs']: ", sig.parameters['kwargs'])
print("sig.parameters['kwargs']: ", sig.parameters['kwargs'].annotation)
print("inspect.isfunction(add): ", inspect.isfunction(add)) #是不是函数
print("inspect.ismethod(add): ", inspect.ismethod(add)) #是不是类方法
print("inspect.isgenerator(add): ", inspect.isgenerator(add)) #是不是生成器
print("inspect.isclass(add): ", inspect.isclass(add)) #是不是类
print("inspect.ismodule(add): ", inspect.ismodule(add)) #是不是模块
print("inspect.isbuiltin(add): ", inspect.isbuiltin(add)) #是不是内建对象
```
```
C:\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tFunctions/tAnnotation/tInspect.py
sig,type(sig):  (x: int, y: int, *args, **kwargs) -> int <class 'inspect.Signature'>
params :  OrderedDict([('x', <Parameter "x: int">), ('y', <Parameter "y: int">), ('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
return :  <class 'int'>
sig.parameters['y']:  y: int <class 'inspect.Parameter'>
sig.parameters['x']:  <class 'int'>
sig.parameters['args']:  *args
sig.parameters['args']:  <class 'inspect._empty'>
sig.parameters['kwargs']:  **kwargs
sig.parameters['kwargs']:  <class 'inspect._empty'>
inspect.isfunction(add):  True
inspect.ismethod(add):  False
inspect.isgenerator(add):  False
inspect.isclass(add):  False
inspect.ismodule(add):  False
inspect.isbuiltin(add):  False

Process finished with exit code 0
```

## parameter 对象
保存在元组中，是只读的

| parameter             | explanation                                                  |
| --------------------- | ------------------------------------------------------------ |
| name                  | 参数的名字                                                 |
| annotation            | 参数注解，可能没有定义                                       |
| default               | 参数的缺省值，可能没有定义                                   |
| empty                 | 特殊的类，用来标记default属性或者注释annotation属性的空值    |
| kind                  | 实参如何绑定到形参，就是形参的类型                           |
| POSITIONAL_ONLY       | 值必须是位置参提供                                           |
| POSITIONAL_OR_KEYWORD | 值可以作为关键字或者位置参数提供                             |
| VAR_POSITIONAL        | 可变位置参数，对应*args                                      |
| KEYWORD_ONLY          | keyword-only参数，对应*或者*args之后的出现的非可变关键字参数 |
| VAR_KEYWORD           | 可变关键字参数，对应**kwargs                                 |

举例：
```py
import inspect

def add(x:int,y:int,*args,**kwargs)->int:
    return x+y

sig =  inspect.signature(add)
print(sig)
print('params : ', sig.parameters)
print('return : ', sig.return_annotation)
print('~~~~~~~~~~~~~~~~')

print(f"{'num':^4}|{'name':^8}|{'param.annotation':^30}|{'param.kind':^25}|{'param.default':^20}")
for i,item in enumerate(sig.parameters.items()):
    name,param = item
    print(f"{i+1:^4}|{name:^8}|{str(param.annotation):^30}|{str(param.kind):^25}|{str(param.default):^20}")
    print(param.default is param.empty, end = '\n\n')

```

```
C:\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/pythonBasic/tGrammar/tFunctions/tAnnotation/tInspect1.py
(x: int, y: int, *args, **kwargs) -> int
params :  OrderedDict([('x', <Parameter "x: int">), ('y', <Parameter "y: int">), ('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
return :  <class 'int'>
~~~~~~~~~~~~~~~~
num |  name  |       param.annotation       |       param.kind        |   param.default    
 1  |   x    |        <class 'int'>         |  POSITIONAL_OR_KEYWORD  |<class 'inspect._empty'>
True

 2  |   y    |        <class 'int'>         |  POSITIONAL_OR_KEYWORD  |<class 'inspect._empty'>
True

 3  |  args  |   <class 'inspect._empty'>   |     VAR_POSITIONAL      |<class 'inspect._empty'>
True

 4  | kwargs |   <class 'inspect._empty'>   |       VAR_KEYWORD       |<class 'inspect._empty'>
True


Process finished with exit code 0

```




## ref 
* [python 类型注解](https://www.cnblogs.com/xzkzzz/p/11378842.html)
* [Python入门篇-类型注解](https://www.cnblogs.com/yinzhengjie/p/10971296.html)
* []()
* []()
* []()
* []()
* []()

