# Django Commad Cheat Sheet




* Start a project `django-admin startproject %project_name%`
* Start the server `python manage.py runserver [port]`，其中port #默认为8888，当指定之后默认的就替换成为指定的那一个。
* Create a app: `python manage.py startapp %app_name%`，注意添加之后别忘了将添加的app添加在settings.py的INSTALLED_APPS列表中。z注意新建的app名称不能跟python中的关键词相同。
* `python manage.py check` 检查当前所有配置是否有错



