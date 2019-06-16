# Generated by Django 2.2.2 on 2019-06-15 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
    ]
