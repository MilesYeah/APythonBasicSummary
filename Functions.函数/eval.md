
# eval

eval 同exec一样可以将一条字符串当作一条命令执行，但这个字符串应该是一个表达式而非语句。

```py
a = 10
print(eval("a>100"))
```

结果会输出：
False




