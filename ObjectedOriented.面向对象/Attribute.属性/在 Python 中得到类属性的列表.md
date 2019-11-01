
# 在 Python 中得到类属性的列表


 今天有个需求要得到一个类的静态属性，也就是说有个类 Type ，我要动态获取 Type.FTE 这个属性的值。

最简单的方案有两个：

* getattr(Type, 'FTE')
* Type.__dict__['FTE']

那么，如果要获取类属性的列表，该怎么做呢？


## dir
首先上场的是 dir ，它能返回当前范围的所有属性名称列表：
```py
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```


## inspect
可以配合使用 inspect 包中的功能来过滤：
```py
>>> [i for i in dir(list) if inspect.isbuiltin(getattr(list, i))]
['__new__', '__subclasshook__']
```
inspect 包中还包含：
```py
>>> [i for i in dir(inspect) if inspect.isfunction(getattr(inspect, i))]
['_searchbases', 'classify_class_attrs', 'cleandoc', 'findsource', 'formatargspec', 'formatargvalues', 'getabsfile', 'getargs', 'getargspec', 'getargvalues', 'getblock', 'getcallargs', 'getclasstree', 'getcomments', 'getdoc', 'getfile', 'getframeinfo', 'getinnerframes', 'getlineno', 'getmembers', 'getmodule', 'getmoduleinfo', 'getmodulename', 'getmro', 'getouterframes', 'getsource', 'getsourcefile', 'getsourcelines', 'indentsize', 'isabstract', 'isbuiltin', 'isclass', 'iscode', 'isdatadescriptor', 'isframe', 'isfunction', 'isgenerator', 'isgeneratorfunction', 'isgetsetdescriptor', 'ismemberdescriptor', 'ismethod', 'ismethoddescriptor', 'ismodule', 'isroutine', 'istraceback', 'joinseq', 'namedtuple', 'stack', 'strseq', 'trace', 'walktree']
```


## callable
还可以配合 callable 来使用：
```py
>>> [i for i in dir(inspect) if not callable(getattr(inspect, i))]
['CO_GENERATOR', 'CO_NESTED', 'CO_NEWLOCALS', 'CO_NOFREE', 'CO_OPTIMIZED', 'CO_VARARGS', 'CO_VARKEYWORDS', 'TPFLAGS_IS_ABSTRACT', '__author__', '__builtins__', '__date__', '__doc__', '__file__', '__name__', '__package__', '_filesbymodname', 'dis', 'imp', 'linecache', 'modulesbyfile', 'os', 're', 'string', 'sys', 'tokenize', 'types']
```


## `__dict__`

上面提到了 `__dict__` ，也可以用它来获取属性列表：
```py
>>> list.__dict__.keys()
['__getslice__', '__getattribute__', 'pop', 'remove', '__rmul__', '__lt__', '__sizeof__', '__init__', 'count', 'index', '__delslice__', '__new__', '__contains__', 'append', '__doc__', '__len__', '__mul__', 'sort', '__ne__', '__getitem__', 'insert', '__setitem__', '__add__', '__gt__', '__eq__', 'reverse', 'extend', '__delitem__', '__reversed__', '__imul__', '__setslice__', '__iter__', '__iadd__', '__le__', '__repr__', '__hash__', '__ge__']
```

然后就可以使用 getattr 来获取模块中的信息了。

除此以外，还可以使用 globals() 来获取已经导入的所有模块。

在一个模块内部，也可以使用 vars() 或者 locales() 来获取模块对象。


（全文完） 