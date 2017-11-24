
from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import MainCity

import json

from rest_framework.decorators import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from  base_model.models import User
from utills.token import req_to_token


@api_view(['GET'])
@authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
@permission_classes((IsAuthenticated,))
def index(request):
    token_data = req_to_token(request)

    this_users = User.objects.filter(username=token_data['username'])
    if this_users:
        this_user = this_users[0]
        # 判断权限
        if this_user.role == 2:
            # data = MainCity(LottoOrder.objects.filter(city='绵阳')).main()
            data = MainCity(LottoOrder.objects.filter(city=this_user.city)).main()
            return HttpResponse(json.dumps(data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")


@api_view(['POST'])
@authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
@permission_classes((IsAuthenticated,))
def search(request):
    token_data = req_to_token(request)

    this_users = User.objects.filter(username=token_data['username'])
    if this_users:
        this_user = this_users[0]
        if this_user.role==2:
            last = request.data['last']
            now = request.data['now']
            data = MainCity(LottoOrder.objects.filter(city=this_user.city)).search(last,now)
            return HttpResponse(json.dumps(data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")
