
# pip快速部署package



`pip freeze`
用pip freeze查看当前安装版本

`pip freeze > requirements.txt`
这将会创建一个 requirements.txt 文件，其中包含了当前环境中所有包及 各自的版本的简单列表。您可以使用 “pip list”在不产生requirements文件的情况下， 查看已安装包的列表。这将会使另一个不同的开发者（或者是您，如果您需要重新创建这样的环境） 在以后安装相同版本的相同包变得容易。

`pip install -r requirements.txt`
这能帮助确保安装、部署和开发者之间的一致性。
