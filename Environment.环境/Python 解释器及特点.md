
[python的种类和特点](https://blog.csdn.net/zhoulin753/article/details/80459987)

2018年05月26日 11:00:20 zhoulin753 阅读数 608

Python是一门解释器语言，代码想运行，必须通过解释器执行，Python存在多种解释器，分别基于不同语言开发，每个解释器有不同的特点，但都能正常运行Python代码，以下是常用的五种Python解释器：

* CPython
  * 当从Python官方网站下载并安装好Python后，就直接获得了一个`官方版本的解释器：Cpython`，
  * 这个解释器是用C语言开发的，所以叫 CPython，
  * 在命名行下运行python，就是启动CPython解释器，
  * CPython是使用最广的Python解释器。
* IPython
  * IPython是`基于CPython的交互式解释器`，
  * 也就是说，IPython只是`在交互方式上有所增强`，
  * 但是执行Python代码的功能和CPython是完全一样的，好比很多国产浏览器虽然外观不同，但内核其实是调用了IE。
* PyPy
  * PyPy是另一个Python解释器，
  * 它的`目标是执行速度`，
  * PyPy采用JIT技术，
  * 对Python代码进行动态编译，所以可以`显著提高Python代码的执行速度`。
* Jython
  * Jython是`运行在Java平台上的Python解释器`，
  * 可以直接把Python代码编译成Java字节码执行。
* IronPython
  * IronPython和Jython类似，只不过IronPython是`运行在微软.Net平台上的Python解释器`，
  * 可以直接把Python代码编译成.Net的字节码。

在Python的解释器中，使用广泛的是CPython，对于Python的编译，除了可以采用以上解释器进行编译外，技术高超的开发者还可以按照自己的需求自行编写Python解释器来执行Python代码，十分的方便！
