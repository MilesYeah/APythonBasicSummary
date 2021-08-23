

## Modifying Python traceback printing

| trackback             | 描述                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| `pytest --showlocals` | show local variables in tracebacks                                                                |
| `pytest -l`           | show local variables (shortcut)                                                                   |
| `pytest --tb=auto`    | (default) 'long' tracebacks for the first and last entry, but 'short' style for the other entries |
| `pytest --tb=long`    | exhaustive, informative traceback formatting                                                      |
| `pytest --tb=short`   | shorter traceback format                                                                          |
| `pytest --tb=line`    | only one line per failure                                                                         |
| `pytest --tb=native`  | Python standard library formatting                                                                |
| `pytest --tb=no`      | no traceback at all                                                                               |
|                       |                                                                                                   |
|                       |                                                                                                   |



## 详细总结报告

`-r` 标志可用于在测试会话结束时显示“简短的测试摘要信息”，这使得在大型测试套件中很容易获得所有失败、跳过、xfail等的清晰图像。

它默认为 `fE` 来列出失败和错误。


用于报告输出的选项

| 选项 | 描述               |
| ---- | ------------------ |
| f    | failed             |
| E    | error              |
| s    | skipped            |
| x    | xfailed            |
| X    | xpassed            |
| p    | passed             |
| P    | passed with output |
|      |                    |
|      |                    |


特殊选项用于选择或不选择某个组

| 选项 | 描述                                                                |
| ---- | ------------------------------------------------------------------- |
| a    | all except pP                                                       |
| A    | all                                                                 |
| N    | none, this can be used to display nothing (since fE is the default) |
|      |                                                                     |
|      |                                                                     |


### instance
| CMD           | 描述                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------ |
| `pytest -ra`  | r 选项接受后面的许多字符，上面使用的 a 表示“除passes之外的所有字符”。                      |
| `pytest -rfs` | 可以使用多个字符，仅查看失败和跳过的测试                                                   |
| `pytest -rpP` | 使用 p 列出通过的测试，而 P 添加了一个额外的部分“PASSES”，其中包含通过但已捕获输出的测试： |
|               |                                                                                            |
|               |                                                                                            |


## Creating resultlog format files¶






## Creating JUnitXML format files


### record_property


### record_xml_attribute


### record_testsuite_property


## Creating resultlog format files


## Sending test report to online pastebin service



## ref
* [Managing pytest’s output](https://docs.pytest.org/en/latest/how-to/output.html)
* []()
* []()
* []()
* []()
* []()
* []()

