
# exec

exec 可以将字符串当作一条命令执行，但这条字符串应该是一个语句，而不是表达式.


```py
exec("sqrt=1")
print(sqrt)
```
结果会输出： 
1


## 可能会污染命名空间

为了安全起见，我们可以提供一个字典来充当命名空间

```py
scope={}
exec("sqrt=1", scope)
scope["sqrt"]
```
结果会输出： 1





