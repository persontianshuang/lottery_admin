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
from base_model.models import UserRecommend


from utills.amount import AmountCommon

class MainAgent2():
    def __init__(self,db):
        self.db = db

    def main(self):
        return self.table_data()

    def table_data(self):
        want = []
        # 查询条件
        # LottoOrder.objects.filter(from_agent__p2=uid)
        base = AmountCommon(self.db)

        # 累加
        want.append({'time': '总数','totle': base.all()})
        want.append({'time': '今日','totle': base.today()})
        want.append({'time': '本月','totle': base.this_month()})
        return want



if __name__=='__main__':
    # ap = MainAgent1(LottoOrder.objects.filter(uid='50')).table_data()
    ap = MainAgent2(LottoOrder.objects.filter(from_agent__p1=None)).main()
    print(ap)


