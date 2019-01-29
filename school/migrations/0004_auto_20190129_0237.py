# Generated by Django 2.1.5 on 2019-01-29 02:37

from django.db import migrations


def forwards_func(apps, schema_editor):
    Menu = apps.get_model("school", "Menu")
    db_alias = schema_editor.connection.alias
    Menu.objects.using(db_alias).bulk_create([
        Menu(num=3, text='用户管理', pid=1, url='/sc/yhgl'),
        Menu(num=2, text='学生管理', pid=1, url='/sc/xsgl'),
        Menu(num=1, text='校园通', pid=0, url=''),
        Menu(num=4, text='通用设置', pid=0, url=''),
    ])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
