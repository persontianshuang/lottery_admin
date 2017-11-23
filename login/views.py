from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from base_model.models import User

from django.contrib.auth.hashers import make_password, check_password




from .serializers import LoginSerializer,UserRegSerializer


@api_view(['GET', 'POST'])
def login(request):
    # 第一次用密码登录，生成token，之后用token登录。如果token过期，重新用密码登录
    # 密码和用户名数据库验证成功后又怎么做
    # api 要权限的话，就用token来避免每次输入用户名和密码
    if request.method == 'POST':
        req_data = request.data
        return_data = {}

        user = User.objects.filter(username=req_data['username'])
        if user:
            this_user = user[0]
            is_checked = check_password(req_data['password'], this_user.password)
            if is_checked:
                print('c')
                from rest_framework_jwt.settings import api_settings

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(this_user)
                token = jwt_encode_handler(payload)
                return_data.update({'name': this_user.name})
                return_data.update({'token': 'JWT '+token})

        return HttpResponse(json.dumps(return_data), content_type="application/json")

@api_view(['POST'])
def register(request):

    if request.method == 'POST':

        # from 通过id查询上级信息，并写入改用户
        req_data = request.data
        req_data['password'] = make_password(req_data['password'], None, 'pbkdf2_sha256')

        serializer = UserRegSerializer(data=req_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
