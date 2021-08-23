# pytest.logging


| CMD                                                                                               | 描述                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| pytest                                                                                            | 无选项运行                                                                     |
| pytest --log-format="%(asctime)s %(levelname)s %(message)s" --log-date-format="%Y-%m-%d %H:%M:%S" | 可以通过传递特定格式选项将日志和日期格式指定为日志模块支持的任何格式：         |
| pytest --show-capture=no                                                                          | 此外，还可以通过该方式完全禁用失败测试上捕获内容（stdout、stderr和日志）的报告 |


也可以通过pytest.ini文件自定义这些选项：
```ini
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```



## caplog fixture¶

在内部测试中，可以更改捕获的日志消息的日志级别。这由caplog fixture 支持：

```py
def test_foo(caplog):
    caplog.set_level(logging.INFO)
    pass
```

默认情况下，级别在 root logger 上设置，但是为了方便起见，也可以设置任何记录器的日志级别：

```py
def test_foo(caplog):
    caplog.set_level(logging.CRITICAL, logger="root.baz")
    pass
```
设置的日志级别将在测试结束时自动恢复。


也可以使用上下文管理器临时更改with块中的日志级别：

```py
def test_bar(caplog):
    with caplog.at_level(logging.INFO):
        pass
```


同样，默认情况下，根记录器的级别会受到影响，但任何记录器的级别都可以更改为：

```py
def test_bar(caplog):
    with caplog.at_level(logging.CRITICAL, logger="root.baz"):
        pass
```

最后，在测试运行期间发送给记录器的所有日志都以logging.LogRecord实例和最终日志文本的形式出现在fixture上。当您要对消息的内容进行断言时，这非常有用：
```py
def test_baz(caplog):
    func_under_test()
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "wally" not in caplog.text
```

有关日志记录的所有可用属性，请参见logging.LogRecord类。


如果您只想确保某些消息是以给定的记录器名称、给定的严重性和消息记录的，您还可以使用记录元组：

```py
def test_foo(caplog):
    logging.getLogger().info("boo %s", "arg")

    assert caplog.record_tuples == [("root", logging.INFO, "boo arg")]
```

可以调用caplog.clear() 重置测试中捕获的日志记录：

```py
def test_something_with_clearing_records(caplog):
    some_method_that_creates_log_records()
    caplog.clear()
    your_test_method()
    assert ["Foo"] == [rec.message for rec in caplog.records]
```

caplog.records属性只包含来自当前阶段的记录，因此在安装阶段中它只包含安装日志，与调用和拆卸阶段相同。


要从其他阶段访问日志，请使用caplog.get_records（when）方法。
例如，如果要确保使用某个特定 fixture 的测试从不记录任何警告，可以在 teardown 期间检查设置和 setup 阶段的记录，如下所示：

```py
@pytest.fixture
def window(caplog):
    window = create_window()
    yield window
    for when in ("setup", "call"):
        messages = [
            x.message for x in caplog.get_records(when) if x.levelno == logging.WARNING
        ]
        if messages:
            pytest.fail(
                "warning messages encountered during testing: {}".format(messages)
            )
```

完整的API在 pytest.LogCaptureFixture.




## Live Logs















## ref
* [How to manage logging](https://docs.pytest.org/en/latest/how-to/logging.html)
* []()
* []()
* []()

