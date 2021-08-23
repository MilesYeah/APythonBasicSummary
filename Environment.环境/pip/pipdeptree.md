
```sh
#!/bin/bash

echo "**********************************************************************"
echo "***********************【导出Python环境包信息】***********************"
pip=`pwd`/venv/bin/pip
pipdeptree=`pwd`/venv/bin/pipdeptree

if [ -e $pip ]
then
  echo "***********************【检测到项目目录下Python解释器】***************"
  echo "# 项目目录下Python第三方package信息" > `pwd`/package_info.txt
  $pip freeze >> `pwd`/package_info.txt
  echo "# 项目目录下Python第三方package依赖树信息" > `pwd`/package_deptree_info.txt
  $pipdeptree -a >> `pwd`/package_deptree_info.txt
else
  echo "***********************【未检测到项目目录下Python解释器，使用系统环境变量目录下Python解释器】************"
  echo "# 系统环境变量中Python第三方package信息" > `pwd`/package_info.txt
  pip freeze >> `pwd`/package_info.txt
  echo "# 系统环境变量中Python第三方package依赖树信息" > `pwd`/package_deptree_info.txt
  pipdeptree -a >> `pwd`/package_deptree_info.txt
fi

echo "***********************【导出Python包信息完成】***********************"
```


