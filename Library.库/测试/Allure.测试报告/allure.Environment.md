# Environment

Environment可以理解成环境变量参数，没有什么实际作用，

个人觉得只是为了让别人知道本次测试的运行环境参数而已，显示啥都是自己定的

注意！！默认是没有的哦


## 如何添加 Environment

通过创建 `environment.properties` 或者 `environment.xml` 文件，并把文件存放到 `allure-results` (这个目录是生成最后的html报告之前，生成依赖文件的目录)目录下，就是 `--alluredir`  后面跟的目录

像我这里目录就是allure，所以放在allure下面 `--alluredir allure` 


### environment.properties
```ini
Browser=Chrome
Browser.Version=81.0.4044.92
Stand=Production
ApiUrl=127.0.0.1/login
python.Version=3.7.2
```

### environment.xml
```xml
<environment>
    <parameter>
        <key>Browser</key>
        <value>Chrome</value>
    </parameter>
    <parameter>
        <key>Browser.Version</key>
        <value>81.0.4044.92</value>
    </parameter>
    <parameter>
        <key>Stand</key>
        <value>Production</value>
    </parameter>
        <parameter>
        <key>ApiUrl</key>
        <value>127.0.0.1/login</value>
    </parameter>
        <parameter>
        <key>python.Version</key>
        <value>3.7.2</value>
    </parameter>
</environment>
```

注意！都不可以写中文哦！！！！亲测！！会乱码





## ref
* []()
* []()
* []()
* []()
* []()
* []()

