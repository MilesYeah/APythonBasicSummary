# colorama.控制台彩色文字

colorama是一个python专门用来在控制台、命令行输出彩色文字的模块，可以跨平台使用。

安装colorama模块

```py
pip install colorama
```

可用格式常数:
1. Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
2. Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
3. Style: DIM, NORMAL, BRIGHT, RESET_ALL


跨平台印刷彩色文本可以使用彩色光的常数简称ANSI转义序列:

```py
from colorama import Fore,Back,Style
print (Fore.RED + "some red text")
print (Back.GREEN + "and with a green background")
print (Style.DIM + "and in dim text")
print (Style.RESET_ALL)
print ("back to normal now!!")
```


Init关键字参数:
init()接受一些* * kwargs覆盖缺省行为
```py
init(autoreset = False):
```

如果你发现自己一再发送重置序列结束时关闭颜色变化每一个打印,然后init(autoreset = True)将自动化
示例：
```py
from colorama import init,Fore
init(autoreset=True)
print (Fore.RED + "welcome to python !!")
print ("automatically back to default color again")
```




## Colorama 使用示例
```py
from colorama import  init,Fore,Back,Style
init(autoreset=True)
class Colored(object):

    #  前景色:红色  背景色:默认
    def red(self, s):
        return Fore.RED + s + Fore.RESET

    #  前景色:绿色  背景色:默认
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET

    #  前景色:黄色  背景色:默认
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    #  前景色:蓝色  背景色:默认
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET

    #  前景色:洋红色  背景色:默认
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    #  前景色:青色  背景色:默认
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    #  前景色:白色  背景色:默认
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  前景色:黑色  背景色:默认
    def black(self, s):
        return Fore.BLACK

    #  前景色:白色  背景色:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s

    def dave(self, s):
        return Style.BRIGHT + Fore.GREEN + s

color = Colored()
print color.red('I am red!')
print color.green('I am gree!')
print color.yellow('I am yellow!')
print color.blue('I am blue!')
print color.magenta('I am magenta!')
print color.cyan('I am cyan!')
print color.white('I am white!')
print color.white_green('I am white green!')
print color.dave("www.cndba.cn")
```
