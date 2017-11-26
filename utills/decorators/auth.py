import json

from django.http import HttpResponse

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from  base_model.models import User
from utills.token import req_to_token


class RequestAuthPost(object):
    def __init__(self, role):
        self.role = role

    def __call__(self, f):

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

class RequestAuthGet(object):
    def __init__(self, role):
        self.role = role

    def __call__(self, f):

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