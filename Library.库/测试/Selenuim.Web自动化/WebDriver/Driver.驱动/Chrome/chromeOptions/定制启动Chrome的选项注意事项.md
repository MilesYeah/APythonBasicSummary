# 定制启动Chrome的选项注意事项

自动化测试的时候为了避免每个case均需要登录的操作，所以把登录后的cookie信息保存下来，在有效期内使用cookie的方式实现登录操作，为了避免展现太多的登录操作，需要通过设置浏览器的option来改变是否可视化；

最早采用phantomjs方式来实现，但是在使用phantomjs时候提示浏览器已经自带属性，所以我们这里不需要再使用phantomjs来实现无界面操作，这个时候需要使用 options.set_headless(headless=True) 设置无界面；
```py
options = webdriver.ChromeOptions()
options.set_headless() # 设置启动无界面化
driver = webdriver.Chrome(chrome_options=options)  # 启动时添加定制的选项
```
此时通过 chrome_options 选项来添加定制的Chrome 来选项参数，但是此时一直提示“DeprecationWarning: use options instead of chrome_options warnings.warn('use options instead of chrome_options', DeprecationWarning)“ 根据错误提示阅读了下源码


```py
if chrome_options:
    warnings.warn('use options instead of chrome_options', DeprecationWarning)
    options = chrome_options

if options is None:
    # desired_capabilities stays as passed in
    if desired_capabilities is None:
        desired_capabilities = self.create_options().to_capabilities()
else:
    if desired_capabilities is None:
        desired_capabilities = options.to_capabilities()
    else:
        desired_capabilities.update(options.to_capabilities())
```

根据源码的提示发现使用chrome_options 时会将chrome_options 值传给options,然后在给一个警告信息，根据错误信息已经源码的注解了解到未来options会取代chrome_options，所以我们只需要chrome_options改成options即可，该问题应该在最近的版本更改的目前我这边使用的是selenium==3.9.0，有兴趣的可以去看下官方文档，那个版本开始做的此项的修改。




# ref
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()

