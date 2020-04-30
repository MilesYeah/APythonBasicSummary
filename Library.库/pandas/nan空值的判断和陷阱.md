
pandas中对nan空值的判断和陷阱

原创 S_o_l_o_n 最后发布于2019-09-09 15:32:18 阅读数 1252 收藏
展开

       pandas基于numpy，所以其中的空值nan和numpy.nan是等价的。numpy中的nan并不是空对象，其实际上是numpy.float64对象，所以我们不能误认为其是空对象，从而用bool(np.nan)去判断是否为空值，这是不对的。

       对于pandas中的空值，我们该如何判断，并且有哪些我们容易掉进去的陷阱，即不能用怎么样的方式去判断呢？


可以判断pandas中单个空值对象的方式：
1. 利用pd.isnull(),pd.isna();
2. 利用np.isnan();
3. 利用is表达式；
4. 利用in表达式。


不可以用来判断pandas单个空值对象的方式：
1. 不可直接用==表达式判断；
2. 不可直接用bool表达式判断；
3. 不可直接用if语句判断。


对于同时多个空值对象的判断和处理：
1. 可以用Series对象和DataFrame对象的any()或all()方法；
2. 可以用numpy的any()或all()方法；
3. 不可以直接用python的内置函数any()和all()方法；
4. 可以用Series或DataFrame对象的dropna()方法剔除空值；
5. 可以用Series或DataFrame对象的fillna()方法填充空值。


示例：
```py
import pandas as pd
import numpy as np
    
na=np.nan
    
# 可以用来判断空值的方式
pd.isnull(na)  # True
pd.isna(na)  # True
np.isnan(na)  # True
na is np.nan  # True
na in [np.nan]  # True
    
    
# 不可以直接用来判断的方式，即以下结果和我们预期不一样
na == np.nan  # False
bool(na)  # True
if na:
    print('na is not null')  # Output: na is not null
    
    
# 不可以直接用python内置函数any和all
any([na])  # True
all([na])  #True
```

总结

       numpy.nan是一个numpy.float64的非空对象，所以不能直接用bool表达式去判断，故一切依赖于布尔表达式的判断方式都不行，比如if语句。对于pandas中空值的判断，我们只能通过pandas或者numpy的函数和is表达式去判断，不能用python的内置函数any或all判断。

       比较奇怪的一点是pandas中空值的判断可以用is表达式判断，但是不能用==表达式判断。我们知道，对于is表达式，如果返回True，表示这两个引用指向的是同一个内存对象，即内存地址是一样的，一般同一个对象的不同引用的值也应该是相等的，所以一般is表达式为True，那么==表达式也为True。但是对于numpy.nan对象显然不是这样的，因为其可以用is表达式判断，即当is表达式为True时，但==表达式为False，这说明虽然不同numpy.nan变量引用指向的是同一个内存地址，但是其具有自己的值属性，值是不一样的，所以不能用==来判断，这点需要注意。

————————————————
版权声明：本文为CSDN博主「S_o_l_o_n」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/S_o_l_o_n/java/article/details/100661937








