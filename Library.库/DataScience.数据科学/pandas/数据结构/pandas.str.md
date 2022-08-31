# pandas.str



```py
import pandas as pd
import numpy as np
s = pd.Series(['A',"B","C","AaBa","Baca",np.nan,'dog','cat'])
```

```py
s
0       A
1       B
2       C
3    AaBa
4    Baca
5     NaN
6     dog
7     cat
dtype: object
```


```py
s.str.upper()
0       A
1       B
2       C
3    AABA
4    BACA
5     NaN
6     DOG
7     CAT
dtype: object
```

```py
s.str.lower()
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6     dog
7     cat
dtype: object
```


```py
s.str.len()
0    1.0
1    1.0
2    1.0
3    4.0
4    4.0
5    NaN
6    3.0
7    3.0
dtype: float64
```

```py
idx = pd.Index([' jack','jill ',' jesse','frank'])
idx
Index([' jack', 'jill ', ' jesse', 'frank'], dtype='object')
idx.str.strip()
Index(['jack', 'jill', 'jesse', 'frank'], dtype='object')
idx.str.lstrip()
Index(['jack', 'jill ', 'jesse', 'frank'], dtype='object')
idx.str.rstrip()
Index([' jack', 'jill', ' jesse', 'frank'], dtype='object')
```





## DataFrame
```py
df = pd.DataFrame(np.random.randn(3,2),columns=[' Column A ',' Column B '],index=range(3))
df
    Column A    Column B 
0   -0.966941   -1.601315
1    0.718955   -0.593178
2    0.352689   -0.353108
```


```py
df.columns.str.strip()
Index(['Column A', 'Column B'], dtype='object')
df.columns.str.lower()
Index([' column a ', ' column b '], dtype='object')
df.columns.str.replace(" ", "_")
Index(['_Column_A_', '_Column_B_'], dtype='object')
df.columns.str.lstrip().str.replace(" ", "_")
Index(['Column_A_', 'Column_B_'], dtype='object')
df.columns.str.strip().str.replace(" ", "_")
Index(['Column_A', 'Column_B'], dtype='object')
df.columns.str.strip().str.replace(" ", "_").str.lower()
Index(['column_a', 'column_b'], dtype='object')
```


## 分割与替换字符


### split
```py
s2 = pd.Series(['a_b_c',"c_D_e",np.nan,'f_g_H'])
s2.str.split("_")
0    [a, b, c]
1    [c, D, e]
2          NaN
3    [f, g, H]
dtype: object
```
```py
s2.str.split('_')[1]
['c', 'D', 'e']
```

```py
s2.str.split('_').str[1]
0      b
1      D
2    NaN
3      g
dtype: object
```

```py
s2.str.split('_').str.get(1)
0      b
1      D
2    NaN
3      g
dtype: object
```

```py
s2.str.split('_',expand=True,n=1)
     0    1
0    a  b_c
1    c  D_e
2  NaN  NaN
3    f  g_H
```

```py
s2.str.rsplit('_',expand=True,n=1)
     0    1
0  a_b    c
1  c_D    e
2  NaN  NaN
3  f_g    H
```


### str.replace
```py
s3 = pd.Series(['A',"B","C","AaBa","Baca",np.nan,"CABA","dog","cat"])
s3
0       A
1       B
2       C
3    AaBa
4    Baca
5     NaN
6    CABA
7     dog
8     cat
dtype: object
```

```py
s3.str.replace('^.a|dog','XX_XX',case=False)  # 替换第二个字符是a或者dog的字符串，忽略大小写，关于正则表达式的内容篇幅很大

0          A
1          B
2          C
3    XX_XXBa
4    XX_XXca
5        NaN
6    XX_XXBA
7      XX_XX
8     XX_XXt
dtype: object
```

```py
dollars = pd.Series(['12', '-$10', '$10,000'])
dollars.str.replace('$', '') # replace $ to ''
<input>:1: FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will *not* be treated as literal strings when regex=True.
0        12
1       -10
2    10,000
dtype: object
```

```py
dollars.str.replace(r'-\$','-')
<input>:1: FutureWarning: The default value of regex will change from True to False in a future version.
0         12
1        -10
2    $10,000
dtype: object
```

```py
dollars.str.replace('-\$', '-')
<input>:1: FutureWarning: The default value of regex will change from True to False in a future version.
0         12
1        -10
2    $10,000
dtype: object

dollars.str.replace("-$",'-')  #  doesn't work 
<input>:1: FutureWarning: The default value of regex will change from True to False in a future version.
0         12
1       -$10
2    $10,000
dtype: object
```



### str.cat操作

```py
s = pd.Series(['A',"B","C","D"])
s.str.cat(sep=',')
s
0    A
1    B
2    C
3    D
dtype: object
```

```py
s.str.cat()
'ABCD'
```


```py
t = pd.Series(['a', 'b', np.nan, 'd'])

t.str.cat(sep=',',na_rep='_')
'a,b,_,d'

s.str.cat(['a',"b","c","d"])
0    Aa
1    Bb
2    Cc
3    Dd
dtype: object

pd.Series(['a1', 'b2', 'c3']).str.extract('(?P<letter>[ab])(?P<digit>\d)', expand=False)
  letter digit
0      a     1
1      b     2
2    NaN   NaN
```



### match or contain操作

```py
pattern = r'[0-9][a-z]'
pd.Series(['1','2','3a','3b','03c']).str.contains(pattern)# 包含数字字母的文本
0    False
1    False
2     True
3     True
4     True
dtype: bool
pd.Series(['1','2','3a','3b','03c']).str.match(pattern)# 匹配数字字母的文本
0    False
1    False
2     True
3     True
4    False
dtype: bool
```










## ref
* [pandas 处理文本数据 ](https://www.cnblogs.com/onemorepoint/p/10106072.html)
* []()
* []()
* []()
* []()
* []()
* []()

