# Categories

Categories 直译：分类

通俗理解：测试用例结果的分类

默认情况下，有两类缺陷：
1. Product defects 产品缺陷（测试结果：failed）
1. Test defects 测试缺陷（测试结果：error/broken）

我们是可以创建自定义缺陷分类的，将 categories.json 文件添加到allure-results目录即可（和上面environment.properties放同一个目录）

 

### categories.json
```json
[
  {
    "name": "Ignored tests", 
    "matchedStatuses": ["skipped"] 
  },
  {
    "name": "Infrastructure problems",
    "matchedStatuses": ["broken", "failed"],
    "messageRegex": ".*bye-bye.*" 
  },
  {
    "name": "Outdated tests",
    "matchedStatuses": ["broken"],
    "traceRegex": ".*FileNotFoundException.*" 
  },
  {
    "name": "Product defects",
    "matchedStatuses": ["failed"]
  },
  {
    "name": "Test defects",
    "matchedStatuses": ["broken"]
  }
]
``` 

讲下参数的含义
1. name：分类名称
2. matchedStatuses：测试用例的运行状态，默认["failed", "broken", "passed", "skipped", "unknown"]
3. messageRegex：测试用例运行的错误信息，默认是 .* ，是通过正则去匹配的哦！
4. traceRegex：测试用例运行的错误堆栈信息，默认是  .*  ，也是通过正则去匹配的哦！

注意
这里的name是可以写中文的哦！

