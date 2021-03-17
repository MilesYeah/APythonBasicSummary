# Python 中的作用域.LEGB

python中的作用域遵循LEGB原则：
| charactor | name      | chinese            |
| --------- | --------- | ------------------ |
| L         | Local     | 局部作用域         |
| E         | Enclosing | 闭包函数外的函数中 |
| G         | Global    | 全局作用域         |
| B         | Built-in  | 内建作用域         |

python按照LEGB原则搜索变量，即优先级L>E>G>B 例如：

```py
print(type(list))        #list为   builtins
list = 1
print(list)
a = 3                #globals
def func1( ):
     a = 3            #enclosing
     def func2( ):
         a = 4        #locals
     return func2
```



