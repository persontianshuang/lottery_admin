
from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import MainCity

import json

from rest_framework.decorators import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, JSONWebTokenAuthentication))
@permission_classes((IsAuthenticated,))
def index(request):
    """
    List all code snippets, or create a new snippet.
    """

    data = MainCity(LottoOrder.objects.filter(city='绵阳')).main()
    return HttpResponse(json.dumps(data),content_type="application/json")
