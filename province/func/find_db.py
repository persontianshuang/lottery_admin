import sys
import os

# 单独的文件使用Django的orm
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery_admin.settings")

import django
django.setup()



import random,time
from datetime import datetime

from utills.amount import AmountCommon

from base_model.models import LottoOrder
from base_model.models import User

class AmountProvince():
    def __init__(self,province):
        self.province = province
        self.alldb = LottoOrder.objects.all()
        self.db = self.alldb.filter(province=province)


    def main(self):

        # def new_lo():
        #     lo = LottoOrder()
        #     lo.amount = random.randint(1, 5000)
        #     lo.province = '四川'
        #     lo.city = '绵阳'
        #     lo.created = random.choice(range(1503635719,1511148621))
        #     print(lo.amount)
        #     lo.save()
        # [new_lo() for x in range(1000)]
        #
        # for l in LottoOrder.objects.all():
        #     # l.created = random.choice(range(1503635719,1511148621))
        #     l.uid = str(random.choice(range(30,110)))
        #     l.save()

        # for u in User.objects.all():
        #     str_nums = 'qwertyuipasdfgjklzxcvbnm'
        #     u.name = ''.join([random.choice(str_nums) for _ in range(11)])
        #     u.save()

        # def new_user():
        #     str_nums = '123456789'
        #     user = User()
        #     user.username = ''.join([random.choice(str_nums) for _ in range(11)])
        #     user.mobile = user.username
        #     user.pasword = 13333333333
        #     user.role = random.choice([4,5])
        #     user.save()
        # [new_user() for _ in range(100)]


        # print(self.alldb)
        return {
            'all': self.table_data(),
            'city': self.city_data(),
            'rank': self.table_data2()

        }

    def table_data(self):
        want = []
        want.append({'time': '总数','totle': str(self.all())})
        want.append({'time': '今日','totle': str(self.today())})
        want.append({'time': '本月','totle': str(self.this_month())})
        return want

    def table_data2(self):
        want = []
        want.append({'all': '全省总销售额','rank': str(self.all())})
        want.append({'all': '全国排名','rank': str(self.province_sort())})
        return want


    def city_data(self):
        city = list(set([x.city for x in self.db]))
        def to_dict(x):
            this_city = AmountCommon(self.db.filter(city=x))
            data = {}
            data.update({'city': x})
            data.update({'this_month': this_city.this_month()})
            data.update({'today': this_city.today()})
            data.update({'all': this_city.all()})
            return data

        city_data = [to_dict(x) for x in city]
        return city_data

    def sum_amount(self,db):
        return sum([x.amount for x in db])

    def all(self):
        return str(self.sum_amount(self.db))

    def today(self):
        t = time.localtime(time.time())
        time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),
                                          '%Y-%m-%d %H:%M:%S'))

        today_zero = int(time1)
        now = int(time.time())
        tdb = self.db.filter(created__range = (today_zero, now))
        return str(self.sum_amount(tdb))

    def this_month(self):
        d = datetime.now()
        b = '{0}-{1}-1 00:00:00'.format(d.year,d.month)
        month_zero = int(time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S")))
        now = int(time.time())
        tdb = self.db.filter(created__range=(month_zero, now))
        return str(self.sum_amount(tdb))

    def province_sort(self):
        import time
        from province.models import ProvinceSorted

        provinces = list(set([x.province for x in self.alldb]))
        def items(province):
            all = self.sum_amount(self.alldb.filter(province=province))
            return (province,all)

        ss = [items(x) for x in provinces]
        sorted_by_sell = sorted(ss,key=lambda key: key[1],reverse=True)
        # have_record = ProvinceSorted.objects.all().count()
        # is_cache = ProvinceSorted.objects.all().order_by('add_time')

        for index,x in enumerate(sorted_by_sell):
            provin = ProvinceSorted.objects.filter(province=x[0])
            if provin:
                ps = provin[0]
                ps.rank = index+1
                ps.amount_sum = x[1]
                ps.add_time = int(time.time())
                ps.save()
            else:
                ps = ProvinceSorted()
                ps.province = x[0]
                ps.rank = index + 1
                ps.amount_sum = x[1]
                ps.add_time = int(time.time())
                ps.save()

        rank = ProvinceSorted.objects.filter(province=self.province)[0].rank
        return rank

# ap = AmountProvince('四川').province_sort()
# ap = AmountProvince('四川').city_data()
# ap = AmountProvince('四川').today()
# ap = AmountProvince('四川').main()
# print(ap)