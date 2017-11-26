
from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import MainCity
from utills.decorators.auth import RequestAuthGet,RequestAuthPost

@RequestAuthGet(2)
def index(request,user):
    # data = MainCity(LottoOrder.objects.filter(city='绵阳')).main()
    data = MainCity(LottoOrder.objects.filter(city=user.city)).main()
    return data


@RequestAuthPost(2)
def search(request,user):
    last = request.data['last']
    now = request.data['now']
    data = MainCity(LottoOrder.objects.filter(city=user.city)).search(last,now)
    return data
