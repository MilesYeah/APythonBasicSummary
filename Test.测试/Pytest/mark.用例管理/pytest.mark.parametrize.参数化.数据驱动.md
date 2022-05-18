# pytest.mark.parametrize
参数化测试功能

[URL pytest.mark.parametrize](https://docs.pytest.org/en/stable/reference.html#pytest.mark.parametrize)

parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
* eg: `@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])`
* `argnames`: 参数名称
  * 一个参数是以字符串的形式标识用例函数的参数，每个参数用逗号隔开
  * 上述例子中，参数名为 `"test_input,expected"`，展开后就是两个参数名 `"test_input"`, `"expected"`
* `argvalues`: 参数值
  * 第二个参数以列表或元组的形式传递测试数据。
    * 参数的数量如果只有一个，那么测试数据应是一维结构
    * 参数的数量如果是两个，那么测试数据应该是二维结构
  * 上述例子中，参数值为 [("3+5", 8), ("2+4", 6), ("6*9", 42)], 展开后会有三组值 
    * ("3+5", 8)
    * ("2+4", 6)
    * ("6*9", 42)
* `indirect=False`
* `ids=None`
* `scope=None`



```py
import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

## 单个参数
在使用pytest.mark.parametrize()传递参数化数据时，测试用例本身必须有参数。
```py
import pytest

# 待测函数
def add(a, b):
    return a + b

# 单个参数的情况
@pytest.mark.parametrize('a', (1,2,3,4,5))
def test_add(a):  # => 作为用例参数，接收装饰器传入的数据
    print('\na的值:', a)
    assert add(a, 1) == a+1
```



## 多个参数
多个参数，@pytest.mark.parametrize()第一个参数依然是字符串， 对应用例的多个参数用逗号分隔。
```py
# 多个参数的情况
@pytest.mark.parametrize('a, b, c', [(1,2,3), (4,5,9), ('1', '2', '12')])
def test_add(a, b, c):
    print(f'\na,b,c的值:{a},{b},{c}')
    assert add(a, b) == c
```


## 对测试类参数化
测试类的参数化，其实际上也是对类中的测试方法进行参数化。类中的测试方法的参数必须与@pytest.mark.parametrize()中的标识的参数个数一致。
```py
# 测试类参数化
import pytest

add = lambda x, y: x+y

@pytest.mark.parametrize('a, b, c', [(1,2,3), (4,5,9)])
class TestAdd():
    def test_add1(self, a, b, c):
        assert add(a, b) == c

    def test_add2(self, a, b, c):
        assert add(a, b) == c

```


参数化会作用于每个测试方法，比如上面两个用例，参数化了两条数据，那么就会执行 4 次。

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeAClass.py
Testing started at 19:30 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeAClass.py --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest\tFixture

============================= test session starts =============================
collecting ... collected 4 items

tMarkParameterizeAClass.py::TestAdd::test_add1[1-2-3] 
tMarkParameterizeAClass.py::TestAdd::test_add1[4-5-9] 
tMarkParameterizeAClass.py::TestAdd::test_add2[1-2-3] 
tMarkParameterizeAClass.py::TestAdd::test_add2[4-5-9] 

============================== 4 passed in 0.10s ==============================

Process finished with exit code 0
PASSED             [ 25%]PASSED             [ 50%]PASSED             [ 75%]PASSED             [100%]
```




## 标记单个测试实例
也可以在 parametrize 中标记单个测试实例，例如使用内置的 mark.xfail ：

```py
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [("3+5", 8), 
     ("2+4", 6),
     pytest.param("6*9", 42, marks=pytest.mark.xfail),
     pytest.param("6*7", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

```

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeMarkAInstance.py
Testing started at 19:35 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeMarkAInstance.py --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest

============================= test session starts =============================
collecting ... collected 4 items

tFixture/tMarkParameterizeMarkAInstance.py::test_eval[3+5-8] 
tFixture/tMarkParameterizeMarkAInstance.py::test_eval[2+4-6] 
tFixture/tMarkParameterizeMarkAInstance.py::test_eval[6*9-42] 
tFixture/tMarkParameterizeMarkAInstance.py::test_eval[6*7-42] 

=================== 2 passed, 1 xfailed, 1 xpassed in 0.28s ===================

Process finished with exit code 0
PASSEDPASSEDXFAIL
test_input = '6*9', expected = 42

    @pytest.mark.parametrize(
        "test_input, expected",
        [("3+5", 8), ("2+4", 6),
         pytest.param("6*9", 42, marks=pytest.mark.xfail),
         pytest.param("6*7", 42, marks=pytest.mark.xfail)],
    )
    def test_eval(test_input, expected):
>       assert eval(test_input) == expected
E       assert 54 == 42

tFixture\tMarkParameterizeMarkAInstance.py:11: AssertionError
XPASS
```

## 叠加 parametrize 
要获得多个参数化参数的所有组合，可以堆叠参数化修饰器：
```py
import pytest


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print(f"x: {x} | y: {y}")
```
双层参数化会逐一展开每层参数，会产生如下组合
* 0，2
* 0，3
* 1，2
* 1，3

```py
C:\Users\Envs\trials\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeLevel2.py
Testing started at 19:24 ...
C:\Program Files\JetBrains\PyCharm Community Edition 2020.2\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:6: DeprecationWarning: The distutils package is deprecated and slated for removal in Python 3.12. Use setuptools or check PEP 632 for potential alternatives
  from distutils import version
Launching pytest with arguments F:/Mirror/SourceCode/trials/tPython/tPytest/tFixture/tMarkParameterizeLevel2.py --no-header --no-summary -q in F:\Mirror\SourceCode\trials\tPython\tPytest\tFixture

============================= test session starts =============================
collecting ... collected 4 items

tMarkParameterizeLevel2.py::test_foo[2-0] 
tMarkParameterizeLevel2.py::test_foo[2-1] 
tMarkParameterizeLevel2.py::test_foo[3-0] 
tMarkParameterizeLevel2.py::test_foo[3-1] 

============================== 4 passed in 0.11s ==============================

Process finished with exit code 0
PASSED                         [ 25%]x: 0 | y: 2
PASSED                         [ 50%]x: 1 | y: 2
PASSED                         [ 75%]x: 0 | y: 3
PASSED                         [100%]x: 1 | y: 3
```



## 数据驱动






## 实例
### 1

```py
import pytest


@pytest.mark.parametrize('a', [1,2,3])      # 1个参数
def test_1_para(a):
    print(f"haha {str(a)}")


@pytest.mark.parametrize('a, b', [[1, 2], [2, 3], [6, 3]])      # 多个参数
def test_multi_para(a, b):
    print(f"{str(a)} {str(b)}")


@pytest.mark.parametrize('a, b, c', [[1,2,3], [2,3,4], [1,3,5]])        # case_01 和 case_02 中参数需要和 parametrize 中的参数一样
class TestParametrize():
    
    def test_case_01(self, a, b, c):
        print(f"{str(a)} {str(b)} {str(c)}")

    def test_case_02(self, a, b, c):
        print(f"haha {str(a)} {str(b)} {str(c)}")


# ids 的作用
data = [(1,2,3), (4,5,9), ('1', '2', '12')]
ids = [f'data{d}' for d in range(len(data))] # => 生成与数据数量相同的名称列表， 
@pytest.mark.parametrize('a, b, c', data, ids=ids)  # 添加了 ids 参数，则执行结果的中括号中显示的参数为 ids 列表中的内容如 `[data0]` ，就不像上面的case中是什么 `[1-3-5]`
def test_add(a, b, c):
    print(f'\na,b,c的值:{a},{b},{c}')

```

```powerhsell
PS G:\Mirror\SourceCode\trials\tPytest> pytest.exe -sv .\test_case\test_parametrize.py
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.9.0, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- c:\users\itach\envs\trials\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.9.0', 'Platform': 'Windows-10-10.0.18362-SP0', 'Packages': {'pytest': '6.2.3', 'py': '1.10.0', 'pluggy': '0.13.1'}, 'Plugins': {'allure-pytest': '2.8.40', 'html': '3.1.1', 'metadata': '1.11.0'}, 'JAVA_HOME':
'C:\\Program Files\\Java\\jdk1.8.0_181'}
rootdir: G:\Mirror\SourceCode\trials\tPytest
plugins: allure-pytest-2.8.40, html-3.1.1, metadata-1.11.0
collected 15 items                                                                                                                                                                                                                     

test_case/test_parametrize.py::test_1_para[1] haha 1
PASSED
test_case/test_parametrize.py::test_1_para[2] haha 2
PASSED
test_case/test_parametrize.py::test_1_para[3] haha 3
PASSED
test_case/test_parametrize.py::test_multi_para[1-2] 1 2
PASSED
test_case/test_parametrize.py::test_multi_para[2-3] 2 3
PASSED
test_case/test_parametrize.py::test_multi_para[6-3] 6 3
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_01[1-2-3] 1 2 3
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_01[2-3-4] 2 3 4
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_01[1-3-5] 1 3 5
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_02[1-2-3] haha 1 2 3
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_02[2-3-4] haha 2 3 4
PASSED
test_case/test_parametrize.py::TestParametrize::test_case_02[1-3-5] haha 1 3 5
PASSED
test_case/test_parametrize.py::test_add[data0]              # 添加了 ids 参数，则中括号中 `[data0]` 中就不像上面的是什么 `[1-3-5]`
a,b,c的值:1,2,3
PASSED
test_case/test_parametrize.py::test_add[data1]
a,b,c的值:4,5,9
PASSED
test_case/test_parametrize.py::test_add[data2]
a,b,c的值:1,2,12
PASSED

========================================================================================================= 15 passed in 0.13s ==========================================================================================================
PS G:\Mirror\SourceCode\trials\tPytest>

```



### 实例 2

Pytest装饰器@pytest.mark.parametrize('参数名',list)实现登录模块2条测试用例数据驱动

 
```py
import pytest,xlrd,os,requests,json
 
#获取excel用例数据
def get_case_data():
    case_path = os.path.join(os.path.dirname(__file__), r'files\apiCase.xls')
    book = xlrd.open_workbook(case_path)
    sheet = book.sheet_by_name('sheet1名字')
    case = []
    for i in range(0, sheet.nrows):
        if sheet.row_values(i)[0] == 'C端登录' and sheet.row_values(i)[3]=='YES':
            case.append(sheet.row_values(i))
    return case
 
class Test(object):
 
    def setup_class(self):
        pass
 
    def teardown_class(self):
        pass
 
    #调用获取测试用例数据
    case_data=get_case_data()
    #使用装饰器参数化用例数据
    @pytest.mark.parametrize('Function,TestCase,Type,Run,URL,Headers,Parameter,SQL1,SQL2,SQL3,AssertType,Expect1,Expect2,Expect3', case_data)
    def test_login1(self,Function,TestCase,Type,Run,URL,Headers,Parameter,SQL1,SQL2,SQL3,AssertType,Expect1,Expect2,Expect3):
        r=requests.post(url=URL,headers=eval(Headers),json=eval(Parameter))
        response=r.json()
        print(response)
        assert eval(Expect1)['code']==response['code']
        assert eval(Expect1)['msg'] == response['msg']
 
 
if __name__=="__main__":
    pytest.main(["-s","test02.py"])
``` 
```sh
"C:\Program Files\Python35\python.exe" C:/Users/wangli/PycharmProjects/Test/test/test02.py
============================= test session starts =============================
platform win32 -- Python 3.5.2, pytest-5.1.2, py-1.8.0, pluggy-0.12.0
rootdir: C:\Users\wangli\PycharmProjects\Test\test
plugins: allure-pytest-2.8.5, html-1.22.0, metadata-1.8.0
collected 2 items
 
test02.py {'msg': '成功', 'code': 0, 'data': {'token': 'bearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9tZW1iZXItYXBpLnN0Mi50ZXN0LmxhbnhpbmthLmNvbVwvMi4wXC91c2Vyc1wvbG9naW4iLCJpYXQiOjE1NzI3NTE4MDUsImV4cCI6MTU3NDA0NzgwNSwibmJmIjoxNTcyNzUxODA1LCJqdGkiOiJpS2ZKZGdBam0xQWoyRmc1Iiwic3ViIjo1ODQ5MDIsInBydiI6IjNhN2IwNmU5NTBkMDhlMjMzMjkyMjdjN2E2YTUyMzQyYWJiNGYxOWIiLCJidXNpbmVzc190eXBlIjoiNiJ9.1bYj4VslhNMU3yjBtxccCG6fAWNwH8jhAacC6cl-f_A'}}
.{'msg': '验证码错误', 'code': 220002, 'data': {}}
.
 
============================== 2 passed in 0.75s ==============================
 
Process finished with exit code 0
```
通过以上实验，我们可以看出如果模块有100条测试用例，同样用以上代码可以实现测试并断言出结果，是不是很简单呢。



## ref
* [原文链接](https://blog.csdn.net/qq_36502272/article/details/102880803)
* []()
* []()
* []()
* []()
* []()
