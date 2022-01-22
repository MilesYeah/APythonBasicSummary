# typing.Final

告知类型检查器某名称不能再次赋值或在子类中重写的特殊类型构造器。

例如：
```py
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker
```

这些属性没有运行时检查。详见 PEP 591。

3.8 新版功能.

