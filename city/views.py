
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


def manage(request):

    # get list
    # 查询以这个为p4的p3用户uid们
    # 再查询uid user 表的详细信息
    if request.methods=='GET':
        @RequestAuthGet(1)
        def get(request):
            p3s =UserRecommend.objects.f(p4=uid,role=2)
            for x in p3s:
                user = User.objects.f(uid=x)
                user.mobile
                user.name
                user.created
                user.city

            return data

    # post 修改 status
    # 通过uid查询user表。修改status状态
    elif request.methods=='POST':
        @RequestAuthGet(1)
        def post(request):
            pass
            users = User.objects.f(uid=uid)
            if users:
                this_user = users[0]
                this_user.status= status
                this_user.save()
                return {'mes': 'ok'}
