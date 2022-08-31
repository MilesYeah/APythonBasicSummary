# pandas 数据类型转换



## 用法一：修改某一列的数据类型 astype
```py
df: pd.DataFrame = pd.DataFrame([
    ['a', '1', '4.2'],
    ['b', '70', '0.03'],
    ['x', '5', '0']
], columns=['one', 'two', 'three'])

df['two'] = df['two'].astype('int64') # 修改'two'列为 int类型
```

one	two	three
a	1	4.2
b	70	0.03
c	5	0



## 用法二：修改多列的数据类型 apply
```py
df: pd.DataFrame = pd.DataFrame([
    ['a', '1', '4.2'],
    ['b', '70', '0.03'],
    ['x', '5', '0']
], columns=['one', 'two', 'three'])

df[['two', 'three']] = df[['two', 'three']].apply(pd.to_numeric) # 内置函数，to_numeric() 可以将一列转换为数值类型，自动判断是 int 还是 float
```

类似的内置函数还包括：pd.to_datetime()，转换成时间类型datetime，还有pd.to_timedelta()转换为时间戳类型


## Ref
* [pandas 数据类型转换](https://www.cnblogs.com/onemorepoint/p/9404753.html)
* []()
* []()
* []()
* []()
* []()
* []()

