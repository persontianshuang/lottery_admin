

from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import MainAgent2

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
    data = MainAgent2(LottoOrder.objects.filter(from_agent__p1=None)).main()
    return HttpResponse(json.dumps(data),content_type="application/json")