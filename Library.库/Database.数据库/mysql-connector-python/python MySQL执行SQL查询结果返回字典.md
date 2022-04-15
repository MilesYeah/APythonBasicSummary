# python MySQL执行SQL查询结果返回字典

写自动化测试的时候我希望执行数据库前置任务，把数据库查询的结果作为请求的参数，但是正常返回结果为列表嵌套里面，这样就会影响到关键字准确的获取，特别的受限于SQL的查询字段的的顺序，所以希望返回的单条数据结果是字典，返回结果为多条数据的时统一存放在列表中便于对数据遍历，同时我在传入参数的时候可以准确的获取关键字；

```py
import pymysql

db = pymysql.connect(host='47.104.149.180', user="root", passwd="root", db='movie', port=3306, charset='utf8')
cursor = db.cursor()

sql = """select name from admin; """

cursor.execute(sql)

desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来

cursor.close()

db.close()

print(data_dict)
```
```py
/*执行SQL以后返回的查询结果*/

[{'name': 'admin'}, {'name': 'admin1'}]
/*如果以元组的形式返回数据*/
```
通过元组返回的数据，如果获取的时候需要通过便利或者根据索引来获取指定数据，但是如果元组的长度变更，会造成获取数据的索引变动，容易对自己的代码的耦合性比较高。

```py
(('admin',), ('admin1',))
```

对比两种返回的结果，明显以字典放的结果更容易被操作，也可以知道具体是哪个字段返回的结果，不会受限于SQL的变动而更改自己的代表，但是最后统一放在列表换是元组，这个是根据自己的习惯来处理，没有特定的要求。






# ref
* [python MySQL执行SQL查询结果返回字典](https://www.cnblogs.com/mengyu/p/10201185.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
