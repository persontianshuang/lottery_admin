
from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import AmountProvince

import json

from rest_framework.decorators import *
from rest_framework.authentication import SessionAuthentication
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
        if this_user.role==1:
            # data = AmountProvince(this_user.province).main()
            # print(data)
            data = AmountProvince('四川').main()
            return HttpResponse(json.dumps(data),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")


# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
# @permission_classes((IsAuthenticated,))
# def search(request):
#     token_data = req_to_token(request)
#
#     this_users = User.objects.filter(username=token_data['username'])
#     if this_users:
#         this_user = this_users[0]
#         if this_user.role==1:
#             # data = AmountProvince(this_user.province).main()
#             # print(data)  request.data
#             last = request.data['last']
#             now = request.data['now']
#             data = AmountProvince('四川').search(last,now)
#             return HttpResponse(json.dumps(data),content_type="application/json")
#         else:
#             return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")


# @api_view(['POST'])
# @authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
# @permission_classes((IsAuthenticated,))
# def manage(request):
#     token_data = req_to_token(request)
#
#     this_users = User.objects.filter(username=token_data['username'])
#     if this_users:
#         this_user = this_users[0]
#         if this_user.role==1:
#             # data = AmountProvince(this_user.province).main()
#             # print(data)  request.data
#             last = request.data['last']
#             now = request.data['now']
#             data = AmountProvince('四川').search(last,now)
#             return HttpResponse(json.dumps(data),content_type="application/json")
#         else:
#             return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")



# 装饰器

class RequestAuthPOST(object):
    def __init__(self, role):
        self.role = role

    def __call__(self, f):
        from rest_framework.decorators import api_view,authentication_classes,parser_classes
        from rest_framework.authentication import SessionAuthentication
        from rest_framework_jwt.authentication import JSONWebTokenAuthentication
        from rest_framework.permissions import IsAuthenticated

        @api_view(['POST'])
        @authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
        @permission_classes((IsAuthenticated,))
        def wrapped_f(*args):
            request = args[0]
            token_data = req_to_token(request)
            this_users = User.objects.filter(username=token_data['username'])

            if this_users:
                this_user = this_users[0]
                if this_user.role == self.role:
                    data = f(*args,this_user)
                    return HttpResponse(json.dumps(data), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'mes': '权限不够'}), content_type="application/json")

        return wrapped_f

@RequestD(1)
def search(request,user):
    last = request.data['last']
    now = request.data['now']
    data = AmountProvince('四川').search(last,now)
    return data