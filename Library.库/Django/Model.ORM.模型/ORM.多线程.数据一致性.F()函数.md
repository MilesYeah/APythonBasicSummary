# F()


settings.py 配置 log
```conf
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
             'propagate': True,
             'level': 'DEBUG',
        }
    },
}
```



## 不使用 F 函数
```py
import threading
from grade.models import Grade


class ChangeThred(threading.Thread):

    def __init__(self, max_count=1000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self):
        count = 0
        obj_grade = Grade.objects.get(pk=1)
        while True:
            if count >= self.max_count:
                break
            print(self.getName(), count)
            obj_grade.score += 1
            obj_grade.save()
            count += 1


def main():
    t1 = ChangeThred(max_count=800, name='T1')
    t2 = ChangeThred(max_count=200, name='T2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

```


可以看到，在修改score 的时候是直接将一个值赋给 score 字段。
`score` = 800.0e0

```sql
UPDATE `grade` SET `student_id` = 1, `student_name` = '张三', `subject_name` = '语文', `score` = 800.0e0, `year` = 2000 WHERE `grade`.`id` = 1; args=(1, '张三', '语文', 800.0, 2000, 1)
```

执行 main() 之后，得到的最终结果为 800 .



## 使用 F 函数

```py
import threading
from django.db.models import F
from grade.models import Grade


class ChangeThred(threading.Thread):

    def __init__(self, max_count=1000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self):
        count = 0
        obj_grade = Grade.objects.get(pk=1)
        while True:
            if count >= self.max_count:
                break
            print(self.getName(), count)
            obj_grade.score = F('score') + 1

            obj_grade.save()
            count += 1


def main():
    t1 = ChangeThred(max_count=800, name='T1')
    t2 = ChangeThred(max_count=200, name='T2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

```


可以看到在修改 score 字段时，采用的是运算的方法得到的新值。
`score` = (`grade`.`score` + 1)

```sql
UPDATE `grade` SET `student_id` = 1, `student_name` = '张三', `subject_name` = '语文', `score` = (`grade`.`score` + 1), `year` = 2000 WHERE `grade`.`id` = 1; args=(1, '张三', '语文', 1, 2000, 1)
```

执行 main() 之后，得到的就是如期望的  `800 + 200 = 1000` 

