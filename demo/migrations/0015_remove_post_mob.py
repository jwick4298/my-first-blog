# Generated by Django 2.2.16 on 2020-10-23 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_auto_20201023_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mob',
        ),
    ]