# index

常见的index种类
* Index 索引
* Int64Index 整数索引
* MultiIndex 层级索引
* DatetimeIndex 时间戳索引

```py
ps = pd.Series(range(5))
ps1 = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame(np.arange(9).reshape(3, 3))
df1 = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])

ps1.index
df1.index

```



## 索引的基本操作

### 重建索引 reindex
```py
ps_1 = ps1.reindex(['a', 'b', 'c', 'd', 'e', 'f'])
ps_2 = ps1.reindex(['a', 'b', 'c', 'd', 'e', 'f'， 1])

df_1 = df1.reindex(['a', 'b', 'c', 'd'])

# df_2 和 df1 的区别会是，df_2的列顺序会调整称为 "C", 'B', "A"
df_2 = df1.reindex(columns=["C", 'B', "A"])
```

```py
>>> ps_2.index
PyDev console: starting.
Index(['a', 'b', 'c', 'd', 'e', 'f', 1], dtype='object')
>>> ps_2
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
f    NaN
1    NaN
dtype: float64
```


### 增
#### Series 新增
```py
import pandas as pd
import numpy as np

ps1 = pd.Series(range(5), index=[1,2,3,4,5])
ps1[9] = 9

s1 = pd.Series({'f': 999})
ps2 = ps1.append(s1)
```
```
>>> ps1
PyDev console: starting.
1    0
2    1
3    2
4    3
5    4
9    9
dtype: int64
>>> ps2
1      0
2      1
3      2
4      3
5      4
9      9
f    999
dtype: int64

```

#### DataFrame 新增
```py
df = pd.DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])

# 增加列（最后一列）
df[4] = 9
df[5] = [10, 11, 12]
# 增加列（第一列）
df.insert(0, "E", [1, 11, 111])

# 增加行
# df[:][4] = [1, 2, 3, 4, 5] # 出错
df.loc['d'] = [1,1,1,1,1, 1]    # 使用标签索引 loc
row = {"E": 6, "A": 6, "B": 6, "C": 6, 4: 6, 5: 6}
df1 = df.append(row, ignore_index=True)
```

```
>>> df
PyDev console: starting.
     E  A  B  C  4   5
a    1  0  1  2  9  10
b   11  3  4  5  9  11
c  111  6  7  8  9  12
d    1  1  1  1  1   1
>>> df1
     E  A  B  C  4   5
0    1  0  1  2  9  10
1   11  3  4  5  9  11
2  111  6  7  8  9  12
3    1  1  1  1  1   1
4    6  6  6  6  6   6

```



### 删
```py
del(ps[1])
del(df['A'])
```

```py
ps_new = ps.drop(2)
```

```py
df_new = df.drop("a")    # 删除行
df_new = df.drop(['a', 'b'])    # 删除多行
```

```py
df_new = df.drop("A", axis=1)    # 删除列
df_new = df.drop(['A', "B"], axis=1)    # 删除多列
df_new = df.drop(['A', "B"], axis='columns')    # 删除多列
```

```py
df.drop("A", axis=1, inplace=True)    # 在源df上删除列
```



### 改


### 查



