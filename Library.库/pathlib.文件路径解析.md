# pathlib

引用网址：https://www.jianshu.com/p/a820038e65c3
```py
from pathlib import Path
p = Path(r'd:\test\tt.txt.bk')
p.name                          # 获取文件名
p.stem                          # 获取文件名除后缀的部分
p.suffix                        # 文件后缀
p.suffixs                       # 文件的后缀们...
# ['.txt', '.bk']
p.parent                        # 相当于dirnanme
# WindowsPath('d:/test')
p.parents                       # 返回一个iterable, 包含所有父目录
# <WindowsPath.parents>
for i in p.parents:
    print(i)
# d:\test
# d:\
a.parts                         # 将路径通过分隔符分割成一个元祖
# ('d:\\', 'test', 'tt.txt.bk')
```


遍历文件夹
```py
p = Path(r'd:\test')
p = Path(p, 'tt.txt')           # 字符串拼接
p.exists()                      # 判断文件是否存在
p.is_file()                     # 判断是否是文件
p.is_dir()                      # 判断是否是目录
```


创建文件夹
```py
p = Path(r'd:\test\tt\dd')
p.mkdir(exist_ok=True)          # 创建文件目录(前提是tt目录存在, 否则会报错)
# 一般我会使用下面这种创建方法
p.mkdir((exist_ok=True, parents=True) # 递归创建文件目录
```


文件信息
```py
p = Path(r'd:\test\tt.txt')
p.stat()                        # 获取详细信息
p.stat().st_size                # 文件大小
p.stat().st_ctime               # 创建时间
p.stat().st_mtime               # 修改时间
```
