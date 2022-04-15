

## 1
To install MySQLdb, provided pip or pip3 is installed on your machine:
```
pip install mysqlclient
```


## 2 

```py
pip install mysql-connector-python
DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='your_user', password='password', server='localhost', database='dname')
```



## ref 
* [ModuleNotFoundError: No module named 'MySQLdb'](https://stackoverflow.com/questions/53024891/modulenotfounderror-no-module-named-mysqldb)
* 