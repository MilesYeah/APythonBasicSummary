# try.except

错误和异常的处理 - try-except

```py           
try:                # 尝试执行的代码
    pass            # 占据代码块，不做任何动作，仅仅保持代码的完整性
except type1 as e1: # 针对错误type1的处理代码，将错误信息记录为e1
    pass
except (type1, ..., typen) as en: # 针对错误元组中的错误种类列表的处理代码，将错误信息记录为en
    pass
except:             # `一种非常危险的操作`,意味着忽略所有错误
    pass
except ...:         # 中间可以加入多个错误种类
    pass
except typeN as eN: # 针对错误typeN的处理代码，将错误信息记录为eN
    pass
else:               # 没有出现异常的时候才执行的部分
    pass
finally:            # 无论是否有异常，该部分都会被执行
    pass
```

* 注意，虽然可以写很多except，但是如果try中的代码执行出错了，但是并不属于该段代码中列出的任何一种异常，那么这个时候是不会执行else和finally的，而是直接崩溃



## try-except 
Usage::
```py
try:   
    try_suite
except Exception as [e]:
    exception_block
```
* try用来捕获try_suite中的错误，并且交给except处理
* except用来处理异常，如果处理异常和设置捕获异常一致，使用exception_block处理异常

try-except code examples

### case1:
```py
try:
    undef
except:
    print('catch an Exception')
```

### case2:
```py
try:
    if undef
except:
    print('catch an Exception')
```
* case1可以捕获异常，因为是运行时错误
* case2不能捕获异常，因为是语法错误，运行前错误


### case3:
```py
try:
    undef
except NameError as e:
    print('catch an Exception')
```

### case4:
```py
try:
    if undef
except IOError as e:
    print('catch an Exception')
```
* case3可以捕获异常，因为设置捕获的是NameError
* case4不能捕获异常，因为设置捕获的是IOError，不会处理NameError


try-except code a game
猜数字小游戏
* 开始游戏产生一个1-100的随机数
* 用户输入，游戏根据输入值提示大或者小
* 根据提示继续输入，直到猜中为止
* 如果用户输入错误，程序可以处理异常


```py
import random
num = random.randint(0, 100)
while True:
    try:
        guess = int(input("Please input a number(0~100): "))
    except ValueError as e:
        print("Not a number, please input again!")
        continue

    if guess > num:
        print("Bigger!")
    elif guess < num:
        print("Lower!")
    else:
        print("Bravo!")
        break

print("This is end!")
```

## try-except 处理多个异常
Usage::
```py
try:   
    try_suite
except Exception1 as [e]:
    exception_block1
except Exception2 as [e]:
    exception_block2
...
except ExceptionX as [e]:
    exception_blockX
```


## try-except-else 
Usage::
```py
try:   
    try_suite
except Exception1 as [e]:
    exception_block1
else:
    none_exception
```
如果没有异常，执行else语句中的代码



## try-except-finally 
* 规则：try-finally无论是否检查到异常，都会执行finally代码
* 作用：为一场处理事件提供清理机制，如用来关闭文件或释放系统资源

Usage::
```py
try:   
    try_suite
except Exception1 as [e]:
    exception_block1
finally:
    none_exception
```
* 如果try语句没有捕获异常，执行完try代码段后，执行finally
* 若try捕获异常，首先执行except处理错误，然后执行finally


```py
try:
    f = open("1.txt")
    line = f.read(2)
    num = int(line)
    print(f"read number {num}")
except IOError as e:
    print(f"catch IOError: {e}")
except ValueError as e:
    print(f"catch ValueError: {e}")
finally:
    try:
        print("Close file.")
        f.close()
    except NameError as e:
        print(f"Catch NameError: {e}")
```


## try-except-else-finally
Usage::
```py
try:   
    try_suite
except Exception1 as [e]:
    exception_block1
else:
    else_block
finally:
    do_finally
```
* 如果try语句没有捕获异常，执行完try代码段之后，执行else代码段，最后执行finally
* 若try捕获异常，首先执行except处理错误，然后执行finally







## ref
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
