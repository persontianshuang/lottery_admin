from django.http import HttpResponse

from base_model.models import LottoOrder

from .func.find_db import MainAgent2
from utills.decorators.auth import RequestAuthGet,RequestAuthPost

@RequestAuthGet(5)
def index(request,user):
    data = MainAgent2(LottoOrder.objects.filter(from_agent__p1=None)).main()

    return data


@RequestAuthPost(5)
def search(request,user):
    last = request.data['last']
    now = request.data['now']
    data = MainAgent2(LottoOrder.objects.filter(from_agent__p1=None)).search(last, now)

    return data





