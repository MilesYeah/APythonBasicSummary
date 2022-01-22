# pip 批量更新

## pip 常用命令
https://www.cnblogs.com/poloyy/p/15170968.html

 

## pip list 结合 Linux 命令
pip list 命令可以查询已安装的库，结合 Linux 的一些命令（cut、sed、awk、grep……），可以直接在命令行中实现批量升级
```py
python3 -m pip list | awk 'NR>=3{print}' | awk '{print $1}' | xargs python3 -m pip install -U
```
1. 先 list 查询
2. 接着第一个 awk 取出行号大于等于 3 的内容
3. 第二个 awk 取出第一列的内容
4. 然后作为参数传给最后的升级命令
 

## 代码中调用 pip 的方法
```py
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
``` 

## 使用 pkg_resources 库
```py
# 需要安装 setuptools
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
``` 

## 使用 pip-review 库（推荐）
https://www.cnblogs.com/poloyy/p/15172198.html

 

## 使用 pipupgrade（推荐）
https://www.cnblogs.com/poloyy/p/15172181.html

 

