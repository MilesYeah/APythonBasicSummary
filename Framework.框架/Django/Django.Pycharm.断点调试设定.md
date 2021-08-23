# PyCharm断点调试django

我在用PyCharm开发django程序的时候，对于打印日志调试程序的方式感觉还是有点麻烦和不直观，所以研究了一下断点调试的方法如下：

1. 打开你的工程，在菜单栏里找到 `Run-->Edit Configurations`
2. 在打开的对话框里边选择Python，点击左上角的 `+` 号
4. 选择 `Python`
5. 新的配置的参数填写
   1. 出现了一个新的项 Unnamed ，你可以把它改名叫 debug ，好听一点
   2. Script path: 脚本选择你项目的 manage.py ，
   3. Parameters: 脚本参数用 runserver ，跟你平常用命令行是一样的，
   4. 聪明的同学应该已经发现了，也可以配置migrate（数据库同步）等等命令参数，来实现命令的快速运行，省的手敲了
6. 之后在菜单栏里找到 `Run-->Debug'debug'` ，并点击
7. 运行后，你能在Console中看到服务器已经运行起来了，有日志打印
8. 之后在你的程序里打断点试试吧，当程序运行到你的断点就会定住了
