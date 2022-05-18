# unittest.mock

1. assert_called()              # mock方法至少调用一次
   1. 如果还未调用, 则返回 AssertionError: Expected 'None' to have been called.
   2. 如果已经调用, 则返回None
2. assert_called_once()         # mock方法只调用一次
   1. 如果调用超过一次则返回 AssertionError: Expected 'None' to have been called.
   2. 否则返回None
3. assert_called_with()         # 断言mock方法已经携带某个参数调用了
   1. 如果没有携带某个参数调用, 那么会断言失败
4. assert_called_once_with()    # 断言mock方法已经携带某个参数调用了一次
   1. 如果没有携带某个参数调用一次的话, 那么会断言失败
5. assert_any_call()            # 有携带参数(有即可)调用过
6. assert_not_called()          # 断言mock方法从未调用过


## Mock基本用法
使用Mock能创建你能访问(模拟)的属性和方法

指定类或者函数的返回值和断言方式

创建handle_mock_01.py文件
```py
# 1. 导入mock模块
from unittest import mock


class Payment(object):
    """
    创建支付类
    """
    pass


payment = Payment()
# 2. 创建Mock对象, 作为Payment的实例方法
payment.pay = mock.Mock(return_value="Success")
# 3. 当调用pay方法时, 会返回定义Mock对象时指定的return_value值
print(payment.pay())
```


## 不同的参数返回不同的值


创建handle_mock_02.py文件
```py
# 1. 导入mock模块
from unittest import mock


class Payment(object):
    """
    创建支付类
    """
    pass


def parameter_return_data(param):
    """定义参数与返回值映射函数
    """
    param_data = {
        "用户ID1": "支付成功",
        "用户ID2": "支付异常",
        "用户ID3": "支付超时",
        "用户ID4": KeyError("参数有误"),  # 可以返回异常

    }
    return param_data[param]


payment = Payment()
# 2. 创建Mock对象, 作为Payment的实例方法
payment.pay = mock.Mock(side_effect=parameter_return_data)
# 3. 当调用pay方法时, 会返回指定的值
print(payment.pay("用户ID1"))   # 返回结果: 支付成功
print(payment.pay("用户ID2"))   # 返回结果: 支付异常
print(payment.pay("用户ID3"))   # 返回结果: 支付超时
print(payment.pay("用户ID4"))   # 返回结果: '参数有误'
```



## 传参个数
创建handle_mock_03.py文件
```py
# 1. 导入mock模块
from unittest import mock


class Payment(object):
    """
    创建支付类
    """
    pass


def fn(a, b):
    """假设实际pay函数, 有两个参数"""
    pass


payment = Payment()
# 2. 创建Mock对象, 作为Payment的实例方法
payment.pay = mock.create_autospec(fn, return_value="支付成功")
# 3. 当调用pay方法时, 传参数的个数如果不为两个, 则会抛出异常
print(payment.pay("用户ID1", "卡号"))   # 返回结果: 支付成功
print(payment.pay("用户ID1"))           # 返回结果: TypeError: missing a required argument: 'b'
```



## 断言方式
创建handle_mock_04.py文件

```py
# 1. 导入mock模块
from unittest import mock


class Payment(object):
    """
    创建支付类
    """
    pass


def parameter_return_data(param):
    """定义参数与返回值映射函数
    """
    param_data = {
        "用户ID1": "支付成功",
        "用户ID2": "支付异常",
        "用户ID3": "支付超时",
        "用户ID4": KeyError("参数有误"),  # 可以返回异常

    }
    return param_data[param]


payment = Payment()
# 2. 创建Mock对象, 作为Payment的实例方法
payment.pay = mock.Mock(side_effect=parameter_return_data)
# 3. 当调用pay方法时, 会返回指定的值
# 4. 不同的断言方式
# a. assert_called() mock方法至少调用一次
# 如果还未调用, 则返回 AssertionError: Expected 'None' to have been called.
# 如果已经调用, 则返回None
print(payment.pay("用户ID1"))   # 返回结果: 支付成功
# print(payment.pay.assert_called())  # 返回结果: None

# b. assert_called_once() mock方法只调用一次
# 如果调用超过一次则返回 AssertionError: Expected 'None' to have been called.
# 否则返回None
print(payment.pay.assert_called_once())  # 返回结果: None

# c. assert_called_with() 断言mock方法已经携带某个参数调用了
# 如果没有携带某个参数调用, 那么会断言失败
print(payment.pay.assert_called_with("用户ID1"))  # 返回结果: None

# d. assert_called_once_with() 断言mock方法已经携带某个参数调用了一次
# 如果没有携带某个参数调用一次的话, 那么会断言失败
print(payment.pay.assert_called_once_with("用户ID1"))  # 返回结果: None

# e. assert_any_call() 有携带参数(有即可)调用过

# f. assert_not_called() 断言mock方法从未调用过
```


