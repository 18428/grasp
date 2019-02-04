# grasp
校园通

# database
1. 创建/更改的文件
python manage.py makemigrations
2. 将生成的py文件应用到数据库
python manage.py migrate

# html 前端
为防止自己定义的 id class 与 EasyUI 定义的冲突
id class 使用 grasp_ 作为前缀。

# 数据初始
makemigrations --empty app_name 这条命令会在 migration 文件夹下产生一个新的文件，我们的插入数据的方法就是在这里填写;


```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    Person = apps.get_model("home_application", "Person")
    db_alias = schema_editor.connection.alias
    Person.objects.using(db_alias).bulk_create([
        Person(age=23, name="zhangsan"),
        Person(age=24, name="lisi"),
    ])


def reverse_func(apps, schema_editor):
    Person = apps.get_model("home_application", "Person")
    db_alias = schema_editor.connection.alias
    Person.objects.using(db_alias).filter(age=23).filter(name="zhangsan").delete()
    Person.objects.using(db_alias).filter(age=24).filter(name="lisi").delete()


class Migration(migrations.Migration):
    # 注明依赖的文件，一定要写，一般不用动，默认生成的已经把依赖设置好了
    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

```
最后：migrate