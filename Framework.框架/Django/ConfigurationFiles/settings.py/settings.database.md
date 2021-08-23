# Settings Database

* [Document for database](https://docs.djangoproject.com/en/2.1/ref/settings/#databases)

### for mysql

```json
DATABASE = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'name' : 'dbname',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': "127.0.0.1"
    }
}

```

### for sqlite3

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

