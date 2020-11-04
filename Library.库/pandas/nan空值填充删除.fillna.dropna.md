# nan空值填充删除

## 删除

DataFrame结构支持使用dropna方法丢弃带有缺失值的数据行，或者使用fillna方法对缺失值进行批量替换，也可以使用loc、iloc方法直接对符合条件的数据进行替换。

dropna方法的语法为：
```py
dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```
其中，参数how='any'时表示只要某行包含缺失值就丢弃，how='all'时表示某行全部为缺失值才丢弃；参数thresh用来指定保留包含几个非缺失值数据的行；参数subset用来指定在判断缺失值时只考虑哪些列。

## 填充

用于填充缺失值的fillna方法的语法为：
```py
fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
```
* 参数value用来指定要替换的值，可以是标量、字典、Series或DataFrame；
* 参数method用来指定填充缺失值的方式，
  * 值为'pad'或'ffill'时表示使用扫描过程中遇到的最后一个有效值一直填充到下一个有效值，
  * 值为'backfill'或'bfill'时表示使用缺失值之后遇到的第一个有效值填充前面遇到的所有连续缺失值；
* 参数limit用来指定设置了参数method时最多填充多少个连续的缺失值；
* 参数inplace=True时表示原地替换, 如果设为 True 则执行后原来的 DataFrame 中对应的值也会被替换


```py
>>> import pandas
>>> import numpy
# 构建一个 DataFrame 
>>> df = pandas.DataFrame({"A": [1,2, numpy.nan, numpy.nan, numpy.nan, 3,4, numpy.nan, numpy.nan, 5], "B": [numpy.nan, 3,4,5,numpy.nan, numpy.nan, numpy.nan, numpy.nan, 6,7]})
>>> 
```
```py
>>> df
     A    B
0  1.0  NaN
1  2.0  3.0
2  NaN  4.0
3  NaN  5.0
4  NaN  NaN
5  3.0  NaN
6  4.0  NaN
7  NaN  NaN
8  NaN  6.0
9  5.0  7.0
# 将所有的  nan 都填充为 10
>>> df.fillna("10")
    A   B
0   1  10
1   2   3
2  10   4
3  10   5
4  10  10
5   3  10
6   4  10
7  10  10
8  10   6
9   5   7
>>> 
```
```py
# 向后填充 ffill，0_B 因为前面没有元素了，所以依然是 NaN
# 其余的，都填充为空值前最后一个非空值
>>> df.fillna(method='ffill')
     A    B
0  1.0  NaN
1  2.0  3.0
2  2.0  4.0
3  2.0  5.0
4  2.0  5.0
5  3.0  5.0
6  4.0  5.0
7  4.0  5.0
8  4.0  6.0
9  5.0  7.0
# 同上
>>> df.fillna(method='pad')
     A    B
0  1.0  NaN
1  2.0  3.0
2  2.0  4.0
3  2.0  5.0
4  2.0  5.0
5  3.0  5.0
6  4.0  5.0
7  4.0  5.0
8  4.0  6.0
9  5.0  7.0
>>> 
```
```py
# 向前填充 bfill/backfill
# 使用空值后遇到的第一个非空值往回填充
>>> df.fillna(method='bfill')
     A    B
0  1.0  3.0
1  2.0  3.0
2  3.0  4.0
3  3.0  5.0
4  3.0  6.0
5  3.0  6.0
6  4.0  6.0
7  5.0  6.0
8  5.0  6.0
9  5.0  7.0
# 同上
>>> df.fillna(method='backfill')
     A    B
0  1.0  3.0
1  2.0  3.0
2  3.0  4.0
3  3.0  5.0
4  3.0  6.0
5  3.0  6.0
6  4.0  6.0
7  5.0  6.0
8  5.0  6.0
9  5.0  7.0
>>> 
```
```py
# 最多只填充两个，剩余保持为 NaN
>>> df.fillna(method='ffill', limit=2)
     A    B
0  1.0  NaN
1  2.0  3.0
2  2.0  4.0
3  2.0  5.0
4  NaN  5.0
5  3.0  5.0
6  4.0  NaN
7  4.0  NaN
8  4.0  6.0
9  5.0  7.0
>>> 
```
```py
>>> df
     A    B
0  1.0  NaN
1  2.0  3.0
2  NaN  4.0
3  NaN  5.0
4  NaN  NaN
5  3.0  NaN
6  4.0  NaN
7  NaN  NaN
8  NaN  6.0
9  5.0  7.0
# 替换后在 DataFrame 中保留替换
>>> df.fillna(method='ffill', limit=2, inplace=True)
>>> df
     A    B
0  1.0  NaN
1  2.0  3.0
2  2.0  4.0
3  2.0  5.0
4  NaN  5.0
5  3.0  5.0
6  4.0  NaN
7  4.0  NaN
8  4.0  6.0
9  5.0  7.0
>>> 
```

