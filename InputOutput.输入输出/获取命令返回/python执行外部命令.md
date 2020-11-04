
# python执行外部命令




## os.system
```py
os.system('ps aux')  
```

执行系统命令，没有返回值



## os.popen
```py
result = os.popen('ps aux')  
    res = result.read()  
    for line in res.splitlines():  
        print(line)
```



## subprocess.Popen
执行系统命令，可以获取执行系统命令的结果
```py
p = subprocess.Popen('ps aux', shell=True, stdout=subprocess.PIPE)  
out, err = p.communicate()  
for line in out.splitlines():  
    print(line)  
```

使用如下方法也能得到 `ps aux` 命令的输出。
```py
p = subprocess.Popen('ps aux', shell=True, stdout=subprocess.PIPE)  
print(p.stdout.read())
```
同上，执行系统命令，可以获取执行系统命令的结果



## subprocess.getstatusoutput
```py
output = subprocess.getstatusoutput('ps aux')  
print(output)  
```

执行系统命令，并获取当前函数的返回值







## ref

* [python执行系统命令后获取返回值的几种方式](https://blog.csdn.net/wowocpp/article/details/80775650)
* [Python中执行系统命令的四种方法](https://www.cnblogs.com/djdjdj123/p/11814341.html)
* 