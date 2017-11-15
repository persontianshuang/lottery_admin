import sys
import os

# 单独的文件使用Django的orm
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lottery_admin.settings")

import django
django.setup()


from base_model.models import LottoOrder
import random,time


sd = LottoOrder.objects.filter(created__range =(1503655555,1510706193))
print(sd.count())
# print(sum([x.amount for x in sd]))

class AmountTime():
    def __init__(self,province):
        self.db = LottoOrder.objects.filter(province=province)

    def all(self):
        return sum([x.amount for x in self.db])

    def today(self):
        pass

    def yesterday(self):
        pass
    def this_week(self):
        pass
    def this_month(self):
        pass


class AmountProvince():
    def __init__(self,province):
        self.db = LottoOrder.objects.filter(province=province)
        self.city = set([x.city for x in self.db])

    def main(self):
        return {'all': self.all()}

    def sum_amount(self,db):
        return sum([x.amount for x in db])

    def all(self):
        return self.sum_amount(self.db)

    def today(self):
        # 获取今天0点的时间戳 和 现在的时间戳  获取这个区间的的交易额
        # today_zero =
        # now = int(time.time())
        # tdb = self.db.filter(created__range = (today_zero, now))
        # self.sum_amount(tdb)
        pass

    def yesterday(self):
        pass
    def this_week(self):
        pass
    def this_month(self):
        pass



class AmountCity():
    def __init__(self,city):
        self.db = LottoOrder.objects.filter(city=city)

    def main(self):
        return {'all': self.all()}

    def sum_amount(self,db):
        return sum([x.amount for x in db])

    def all(self):
        return self.sum_amount(self.db)

    def today(self):
        pass

    def yesterday(self):
        pass
    def this_week(self):
        pass
    def this_month(self):
        pass

# for l in LottoOrder.objects.all():
#     l.created = random.choice(range(1503635719,1510706193))
#     l.save()

# def new_lo():
#     lo = LottoOrder()
#     lo.amount = random.randint(1,1000)
#     lo.province = '福建'
#     lo.city = '莆田'
#     print(lo.amount)
#     lo.save()
#
# [new_lo() for x in range(1000)]