# Generated by Django 2.2.16 on 2020-10-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20201021_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('GOT', 'GOT'), ('Suits', 'Suits'), ('Dark', 'Dark'), ('Breaking Bad', 'Breaking Bad')], default='O1', max_length=20),
        ),
    ]
