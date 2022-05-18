# How to handle test failures

### Stopping after the first (or N) failures

| CMD                  | 描述             |
| -------------------- | ---------------- |
| `pytest -x`          | 首次故障后停止   |
| `pytest --maxfail=2` | 第二次故障后停止 |



### Dropping to PDB (Python Debugger) on failures

| CMD                        | 描述                                      |
| -------------------------- | ----------------------------------------- |
| `pytest --pdb`             | pytest允许通过命令行选项进入PDB提示符     |
| `pytest -x --pdb`          | 在第一次失败时跳转到PDB，然后结束测试会话 |
| `pytest --pdb --maxfail=3` | 前三个failure后，转到PDB                  |



#### Dropping to PDB (Python Debugger) at the start of a test

| CMD            | 描述                                                      |
| -------------- | --------------------------------------------------------- |
| pytest --trace | pytest允许在每个测试开始时通过命令行选项立即进入PDB提示符 |




#### Setting breakpoints


#### Using the builtin breakpoint function


### Profiling test execution duration


### Fault Handler


### Warning about unraisable exceptions and unhandled thread exceptions



## ref
* [How to handle test failures](https://docs.pytest.org/en/latest/how-to/failures.html)
* []()
* []()
* []()
* []()


