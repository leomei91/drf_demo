from django.shortcuts import render

# Create your views here.
from goods.models import Goods

from rest_framework import viewsets
from goods.serializers import GoodsSerializer

from rest_framework.decorators import action

import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GoodsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goods to be viewed or edited.
    """
    queryset = Goods.objects.all().order_by('-add_time')
    serializer_class = GoodsSerializer
    lookup_field = 'good_name'
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    @action(detail=True)
    def retrieve_by_name(self, request, good_name):
        qs = Goods.objects.filter(good_name=good_name)
        json_data = serializers.serialize('json', qs)
        return JsonResponse(json_data, safe=False)