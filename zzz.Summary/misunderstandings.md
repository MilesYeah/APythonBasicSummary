
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


