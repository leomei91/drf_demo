from django.db import models
from datetime import datetime
# Create your models here.

class Goods(models.Model):
    good_name = models.CharField(max_length=30, unique=True)
    good_desc = models.CharField(max_length=100)
    good_price = models.CharField(max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    def __str__(self):
        return self.good_name