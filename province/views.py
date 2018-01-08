
from django.http import HttpResponse
from base_model.models import LottoOrder,User,UserRecommend

from .func.find_db import AmountProvince
from utills.decorators.auth import RequestAuthGet,RequestAuthPost

@RequestAuthGet(1)
def index(request,user):
    data = AmountProvince('四川').main()
    return data

@RequestAuthPost(1)
def search(request,user):
    last = request.data['last']
    now = request.data['now']
    data = AmountProvince('四川').search(last,now)
    return data


# def manage(request):
#
#     # get list
#     # 查询以这个为p4的p3用户uid们
#     # 再查询uid user 表的详细信息
#     if request.methods=='GET':
#         @RequestAuthGet(1)
#         def get(request):
#             p3s =UserRecommend.objects.f(p4=uid,role=2)
#
#             def get_user_info():
#                 user = User.objects.f(uid=x)
#                 user.mobile
#                 user.name
#                 user.created
#                 user.city
#                 return data
#
#             data = [get_user_info(x) for x in p3s]
#
#             return data
#
#     # post 修改 status
#     # 通过uid查询user表。修改status状态
#     elif request.methods=='POST':
#         @RequestAuthGet(1)
#         def post(request):
#             pass
#             users = User.objects.f(uid=uid)
#             if users:
#                 this_user = users[0]
#                 this_user.status= status
#                 this_user.save()
#                 return {'mes': 'ok'}




# pip install pymysql djangorestframework-jwt djangorestframework django-filter
# django-cors-headers