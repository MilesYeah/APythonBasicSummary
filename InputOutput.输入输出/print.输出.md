# print 输出




## sep 分隔符 end 终止符




## 打印输出至文件中

将 print() 函数的输出重定向到一个文件中去。

在 print() 函数中指定 file 关键字参数，像下面这样：
```py
with open('d:/work/test.txt', 'wt') as f:
    print('Hello World!', file=f)
```

关于输出重定向到文件中就这些了。但是有一点要注意的就是文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错。





## ref
* [打印输出至文件中](https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p02_printing_to_file.html)
* [使用其他分隔符或行终止符打印](https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p03_print_with_different_separator_or_line_ending.html)
* []()
* []()
* []()
* []()

