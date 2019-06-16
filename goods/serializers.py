from goods.models import Goods
from rest_framework import serializers


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ('good_name', 'good_desc', 'good_price', 'add_time', 'update_time')