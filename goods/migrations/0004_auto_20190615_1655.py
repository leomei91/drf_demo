# Generated by Django 2.2.2 on 2019-06-15 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20190615_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间'),
        ),
    ]
