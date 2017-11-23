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

print(LottoOrder.objects.all())

# sd = LottoOrder.objects.filter(created__range =(1503655555,1510706193))
# print(sd.count())
# print(sum([x.amount for x in sd]))


# for l in LottoOrder.objects.all():
#     l.created = random.choice(range(1503635719,1510791386))
#     l.save()

def new_lo():
    lo = LottoOrder()
    lo.amount = random.randint(1,1000)
    lo.province = '福建'
    lo.city = '莆田'
    print(lo.amount)
    lo.save()

[new_lo() for x in range(1000)]