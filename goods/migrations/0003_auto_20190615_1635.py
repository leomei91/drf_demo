# Generated by Django 2.2.2 on 2019-06-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20190615_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间'),
        ),
    ]
