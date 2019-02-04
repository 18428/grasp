# Generated by Django 2.1.5 on 2019-02-04 17:42

from django.db import migrations


def forwards_func(apps, schema_editor):
    Menu = apps.get_model("school", "Menu")
    db_alias = schema_editor.connection.alias
    Menu.objects.using(db_alias).bulk_create([
        Menu(num=5, text='权限设置', pid=4, url=''),
    ])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_user'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
