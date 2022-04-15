# SQL注入攻击

```sql
username="1 OR 1=1";
password="1 OR 1=1";
sql="SELECT COUNT(*) FROM t_user WHERE username="+username+"AND AES_DECRYPT(UNHEX(password),' Hellowor1d")="+pas sword;
cursor.execute(sql);
print(cursor.fetchone()[e]);
```

## SQL注入攻击的危害
由于SQL语句是解释型语言，所以在拼接SQL语句的时候，容易被注入恶意的SQL语句
```sql
id="1 OR 1=1"
sql="DELETE FROM t_news WHERE id="+id；
```

## SQL预编译机制
预编译SQL就是数据库提前把SQL语句编译成二进制，这样反复执行同一条SQL语句的效率就会提升
```sql
sql="INSERT INTO t_emp（empno，ename，job，mgr，hiredate，sal，comm，deptno）
VALUES（%S，%s，%5，%5，%s，%5，%s，%5）"；
```

SQL语句编译的过程中，关键字已经被解析过了，所以向编译后的SQL语句传入参数，都被当做字符串处理，数据库不会解析其中注入的SQL语句
```sql
id="1 OR 1=1"
sql="DELETE FROM t_news WHERE id=%s"；
```


### 预防 SQL 注入攻击

```py
cursor = conn.cursor()

# 未防止攻击
username = '1 or 1=1'
password = '1 or 1=1'
sql = f"select * from t_user where username={username} and aes_decrypt(unhex(password),'HelloWorld')={password};"
cursor.execute(sql)
for item in cursor.fetchall():
    print(item)

print('-----------------------')

# 防止攻击
sql = f"select * from t_user where username=%s and aes_decrypt(unhex(password),'HelloWorld')=%s;"
cursor.execute(sql, (username, password))
for item in cursor.fetchall():
    print(item)

cursor.close()
```



