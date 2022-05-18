
















1-20题目











## 1.输入日期， 判断这一天是这一年的第几天？






## 2.给定两个列表，怎么找出他们相同的元素和不同的元素






## 3.请写出一段 python 代码实现删除 list 里面的重复元素






## 4.一行代码实现 1-100 之和






## 5.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}






## 6.请写一个函数reverse，参数是一个列表，该函数将列表中的所有元素倒序排列并返回
比如 reverse([1, 2, 3, 4]) ➞ [4, 3, 2, 1] reverse([9, 9, 2, 3, 4]) ➞ [4, 3, 2, 9, 9] reverse([]) ➞ []






## 7.请写一个函数tri_area，参数是三角形的底和高，请计算返回三角形面积
比如 tri_area(3, 2) ➞ 3 tri_area(7, 4) ➞ 14 tri_area(10, 10) ➞ 50






## 8.请写一个函数concat，参数分别是两个列表，请返回两个列表合并的结果
比如
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8] concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2] concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]






## 9.ATM机允许4或6位PIN码，PIN码只能包含4位数或6位数字。 请写一个参数为字符串的函数，如果PIN有效则返回True，如果不是则返回False。
比如 is_valid_PIN("1234") ➞ True is_valid_PIN("12345") ➞ False is_valid_PIN("a234") ➞ False is_valid_PIN("") ➞ False






## 10.请写一个函数，该函数 参数为数字列表，请算出另外一个列表，里面每个元素依次是参数列表里面元素的累计和。
比如
参数为[1, 2, 3, 4] 结果计算方法为[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4] 返回结果就应该是[1, 3, 6, 10]










若有收获，就点个赞吧





# 1-20答案

## 1

```py
import datetime
def dayofyear():

year = input("请输入年份: ")
month = input("请输入月份: ")

day = input("请输入天: ")
date1 = datetime.date(year=int(year),month=int(month),day=int(day))

date2 = datetime.date(year=int(year),month=1,day=1)
return (date1-date2).days+1
```




## 2

```py
list1 = [1,2,3]
list2 = [3,4,5]

set1 = set(list1)
set2 = set(list2)

print(set1 & set2)
print(set1 ^ set2)
```




## 3

```py
22





l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))

print(l2)


用 list 类的 sort 方法:
l1 = ['b','c','d','c','a','a']

l2 = list(set(l1))
l2.sort(key=l1.index)

print(l2)


也可以这样写:

l1 = ['b','c','d','c','a','a']
l2 = sorted(set(l1),key=l1.index)

print(l2)


也可以用遍历：

l1 = ['b','c','d','c','a','a']

l2 = []
for i in l1:

if not i in l2:

l2.append(i)
print(l2)
```




## 4

```py
count = sum(range(1,101))
print(count)
```




## 5

```py
10




str1 = "k:1|k1:2|k2:3|k3:4"

def str2dict(str1):
dict1 = {}

for iterms in str1.split('|'):
key,value = iterms.split(':')

dict1[key] = value
return dict1


#方式二：字典推导式

d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
```




## 6

```py


def reverse(inlist):

inlist.reverse()
return inlist


inlist = [1, 2, 3, 4]

reverse(inlist)
print(inlist)
```




## 7

```py
def tri_area(l,g):
return int(l*g/2)


print(tri_area(3, 2))
```




## 8

```py
def concat(p1,p2):
return p1 + p2


print(concat([1, 3, 5], [2, 6, 8]))
```




## 9

```py
11





def is_valid_PIN(para):
if len(para) not in [4,6]:

return False


if not para.isdigit():
return False


return True


print(is_valid_PIN("1234a"))


```




## 10





```
def accumulate(para):

ret = []
idx = 0

for one in para:
ret.append(sum(para[:idx+1]))

idx += 1


return ret


print(accumulate([1, 2, 3, 4]))






```



若有收获，就点个赞吧







## ref
* [1-20题目](https://www.yuque.com/poloyy/interview/rdetu9)
* [1-20答案](https://www.yuque.com/poloyy/interview/pg2376)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()

