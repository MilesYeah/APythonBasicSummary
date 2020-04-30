
## dict fromkeys
```py
v = dict.fromkeys(['k1','k2'],[]) 
# v = dict.fromkeys(['k1','k2'],list()) 
print(v)
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v)

# 运行结果
PS D:\OneDrive\Doc> & "C:/Program Files/Python37/python.exe" d:/OneDrive/Doc/MD.Lang/Python/zzz.temp/.0.py
{'k1': [], 'k2': []}
{'k1': [666], 'k2': [666]}
{'k1': 777, 'k2': [666]}
PS D:\OneDrive\Doc>
```



## [浅入深谈：一道Python面试题，让我明白了殊途同归，却开始怀疑自己](https://www.itcodemonkey.com/article/4298.html)

```py
def func():
    l = [lambda x: x*2 for x in range(4)]
    return l

# print(func())
for item in func():
    print(item(2))

PS D:\OneDrive\Doc> & "C:/Program Files/Python37/python.exe" d:/OneDrive/Doc/MD.Lang/Python/zzz.temp/.0.py
4
4
4
4
PS D:\OneDrive\Doc>
```


```py
def func():
    for i in range(4):
        yield lambda x:x*i

for item in func():
    print(item(2))

PS D:\OneDrive\Doc> & "C:/Program Files/Python37/python.exe" d:/OneDrive/Doc/MD.Lang/Python/zzz.temp/.0.py
0
2
4
6
PS D:\OneDrive\Doc>
```




## 一行代码实现9*9乘法表

首先，我们可以先将多行代码的实现方式写出来先：
```py
for i in range(1, 10):
    for j in range(i, 10):
        print(f"{i}*{j}={i*j}", end='\t')
    print('\n')
```
再来通过这个多行的实现改写
* 从最里层开始展开，里层的for返回的其实是9个列表，那么这九个列表分别对应了乘法表的九列，那么我们可以使用'\t'.join将这九个列表分别连接起来，那么就会成为一行字符串
* 再展开外层则代表乘法表的九行，那么使用'\n'.join将上面返回的九行连接起来，那就是一个乘法表了

1. [f"{i}*{j}={i*j}" for j in range(i, 10)]
2. '\t'.join([f"{i}*{j}={i*j}" for j in range(i, 10)])
3. ['\t'.join([f"{i}*{j}={i*j}" for j in range(i, 10)]) for i in range(1, 10)]
3. '\n'.join(['\t'.join([f"{i}*{j}={i*j}" for j in range(i, 10)]) for i in range(1, 10)])





## 列表解析式

* [i for i in range(10)]
  * 返回一个列表
* (i for i in range(10))
  * 返回一个生成器




## 错误使用类变量 
```py
class A(object):x = 1
class B(A):pass
class C(A):pass
print( A.x, B.x, C.x)
1 1 1
```

这里输出的值都是1，然后我们试着来改变一下A.x和B.x的值看看有什么变化。

```py
B.x = 2
print (A.x, B.x, C.x)
A.x = 3
print (A.x, B.x, C.x)
1 2 1
3 2 3
```

我们只改变了A.x,为什么C.x改变呢？


这里需要简单了解一下python的命名空间。

python中，命名空间是名字到对象映射的结合，不同命名空间中的名字是没有关联的，这种映射的实现有点类似于python中的字典。

当你名字访问一个对象的属性时，先从对象的命名空间寻找。如果找到了这个属性，就返回这个属性的值；如果没有找到的话，则从类的命名空间中寻找，找到了就返回这个属性的值，找不到则抛出异常。


在Python中，类变量在内部作为字典处理，并遵循通常称为方法解析顺序（MRO）的方法。


MRO：Method Resolution Order 方法解析顺序，Python支持多继承，该方法用于解决父类存在同名函数的时存在的二义性问题。


因此在上面的代码中，由于x在对象的命名空间中找不到该属性C，因此将在类中查找它。换句话说，C没有自己的x属性，独立于A。因此，引用C.x实际上是指A.x。




## 误解python范围规则

如果你不了解python的范围规则，那么你很容易犯错误，这是因为Python使用一种独有的范围规则来确定变量范围。

python范围解析是基于LEGB规则，以下是Python范围规则的概述：

·L -代表Local。它包含在函数内指定的（标识符/变量）名称（使用def或lambda），而不是使用global关键字声明。

·E -代表Enclosing function locals。它包含来自任何/所有封闭函数的本地范围的名称（例如，使用def或lambda）。

·G -指全球实体。它包括在模块文件的顶层运行或使用global关键字定义的名称。

·B -指内置插件。它跨越预先指定为内置名称的名称，如打印，输入，打开等。

LEGB规则指定名称空间的以下顺序，用于搜索名称：

Local - > Enclosed - > Global - > Built-in

考虑以下的例子：

```py
x = 10
def foo():
  x += 1
print(x) 
foo()

UnboundLocalError Traceback (most recent call last):
<ipython-input-26-234e54482865> in <module>
<ipython-input-26-234e54482865> in foo()
UnboundLocalError: local variable 'x' referenced before assignment
```

发生上述错误的原因是，对作用域中的变量进行赋值时，Python会自动将该变量视为该作用域的本地变量，并在外部作用域中隐藏任何类似命名的变量。

因此，许多人在代码提示出错并显示需要在函数中添加赋值语句而感到不解。


考虑一个在使用列表时遇到的例子：

```py
lst = [1, 2, 3]
def foo1():
 lst.append(5)   
foo1()
lst
[1, 2, 3, 5]


lst = [1, 2, 3]
def foo2():
  lst += [5]      
foo2()

UnboundLocalError  Traceback (most recent call last):
<ipython-input-30-579469eed71a> in <module>   
<ipython-input-30-579469eed71a> in foo2()
UnboundLocalError: local variable 'lst' referenced before assignment
```

为什么foo2出错了但是foo1运行良好？


答案在前面就已经有所提示，在这个例子当中foo1（）做一个分配到lst，而在foo2（）当中lst += [5]其实只是lst = lst + [5]的简写，我们希望分配一个值给lst，但是分配的值lst是基于lst自身，但其尚未定义。





## python闭包变量绑定

python的闭包变量问题也是新手们容易混淆的一个点，来看看下面的例子：

```py
def create_multipliers():
  return [lambda x : i * x for i in range(5)]
for multiplier in create_multipliers():
   print (multiplier(2))
8
8
8
8
8
```

为什么结果是88888，和我所想的02468不一样呢？


这是由于Python的迟绑定(late binding)机制，闭包中内部函数的值只有在被调用时才会进行查询。


因此create_multipliers函数返回的lambda函数被调用时，会在附近的作用域中查询变量i的值，而在create_multipliers生成返回数组之后，整数i的值是4，不会再改变，因此返回数组中每个匿名函数实际上都是：lambda x: 4*x。、


解决办法是将临时值也保存在匿名函数的作用域内，在声明匿名函数时就查询变量的值。


了解原理之后，让我们来改一改代码，surprise！

```py
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]
for multiplier in create_multipliers():
    print (multiplier(2))
0
2
4
6
8
```























































