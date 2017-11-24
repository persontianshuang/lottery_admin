import sys
import os

# 单独的文件使用Django的orm
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery_admin.settings")

import django
django.setup()


from base_model.models import LottoOrder
from base_model.models import User

from utills.amount import AmountCommon


class MainCity():
    def __init__(self,db):
        self.db = db

    def main(self,last,now):
        last_list = [x.strip() for x in last.split('-')]
        now_list = [x.strip() for x in now.split('-')]

        last_num = ac.time_formater(last[0], last[1], last[2])
        now_num = token_data = req_to_token(request)
        amount_time_range = ac.time_range(last_num, now_num)

        data = {
            'time': last + ' => ' + now,
            'amount': amount_time_range
        }

    def table_data(self):
        want = []
        base = AmountCommon(self.db)
        want.append({'time': '总数','totle': base.all()})
        want.append({'time': '今日','totle': base.today()})
        want.append({'time': '本月','totle': base.this_month()})
        return want





# ap = MainCity(LottoOrder.objects.filter(city='绵阳')).table_data()
# ap = MainCity(LottoOrder.objects.filter(city='绵阳')).main()
# print(ap)