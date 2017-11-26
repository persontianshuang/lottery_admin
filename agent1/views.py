from django.http import HttpResponse
from base_model.models import LottoOrder

from .func.find_db import MainAgent1


from utills.decorators.auth import RequestAuthGet,RequestAuthPost

@RequestAuthGet(4)
def index(request,user):
    data = MainAgent1(LottoOrder.objects.filter(from_agent__p2=38)).main()
    return data


@RequestAuthPost(4)
def search(request,user):
    last = request.data['last']
    now = request.data['now']
    data = MainAgent1(LottoOrder.objects.filter(from_agent__p2=38)).search(last, now)

    return data


