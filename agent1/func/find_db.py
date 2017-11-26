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



class MainAgent1():
    def __init__(self,db):
        self.db = db

    def main(self):

        return {
            'all': self.table_data(),
            'dtails':self.agent_data()
        }

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

    def search(self,last_str,now_str):
        last_list = [x.strip() for x in last_str.split('-')]
        now_list = [x.strip() for x in now_str.split('-')]
        amount_time_range = AmountCommon(self.db).time_range(last_list,now_list)

        data = {
            'date': last_str + ' 到 ' + now_str,
            'totle': amount_time_range
        }
        return data



    def agent_data(self):
        # 二级代理的uid,不包括普通用户的uid  p1!=null
        # urs = UserRecommend.objects.exclude(p1=None).filter(p2=self.db[0].uid,)
        urs = UserRecommend.objects.filter(p2=self.db[0].uid,uid_user__role=5)
        sed_agent_uids = list(set([x.uid for x in urs]))

        def to_dict(uid,agent_name):
            # 该一级代理下的普通用户列表

            # 聚合 每个用户查询结果累加 每个用户都要查询 避免
            for x in sed_agent_uids:
                this_city = AmountCommon(LottoOrder.objects.filter(from_agent__p1=uid))
                data = {}
                data.update({'city': agent_name})
                data.update({'this_month': float(this_city.this_month())})
                data.update({'today': float(this_city.today())})
                data.update({'all': float(this_city.all())})
                return data

        agent_sell_data = []
        for uid in sed_agent_uids:
            users = User.objects.filter(uid=uid)
            if users:
                this_user = users[0]
                one_agent = to_dict(uid,this_user.name)
                agent_sell_data.append(one_agent)

        return agent_sell_data


if __name__=='__main__':
    # ap = MainAgent1(LottoOrder.objects.filter(uid='50')).table_data()
    ap = MainAgent1(LottoOrder.objects.filter(from_agent__p2=38)).main()
    print(ap)


