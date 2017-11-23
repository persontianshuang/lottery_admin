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

    def main(self):

        return {
            'all': self.table_data(),
            'one': self.agent_data(4),
            'two':self.agent_data(5)
        }

    def table_data(self):
        want = []
        base = AmountCommon(self.db)
        want.append({'time': '总数','totle': base.all()})
        want.append({'time': '今日','totle': base.today()})
        want.append({'time': '本月','totle': base.this_month()})
        return want


    def agent_data(self,role):
        # 查询该城市下的订单含有该级代理的所有uid

        agent_uids = list(set([x.uid for x in self.db]))

        def to_dict(uid,agent_name):
            this_city = AmountCommon(self.db.filter(uid=uid))
            data = {}
            data.update({'city': agent_name})
            data.update({'this_month': float(this_city.this_month())})
            data.update({'today': float(this_city.today())})
            data.update({'all': float(this_city.all())})
            return data

        agent_sell_data = []
        for uid in agent_uids:
            users = User.objects.filter(uid=uid)
            if users:
                this_user = users[0]
                one_agent = to_dict(uid,this_user.name)
                agent_sell_data.append(one_agent)

        return agent_sell_data




# ap = MainCity(LottoOrder.objects.filter(city='绵阳')).table_data()
# ap = MainCity(LottoOrder.objects.filter(city='绵阳')).main()
# print(ap)