from django.shortcuts import get_object_or_404, render

from base_model.models import LottoOrder



class AmountCity():
    def __init__(self, city):
        self.db = LottoOrder.objects.filter(city=city)

    def main(self):
        return {'all': self.all()}

    def sum_amount(self, db):
        return sum([x.amount for x in db])

    def all(self):
        return self.sum_amount(self.db)


class AmountProvince():
    def __init__(self,province):
        self.db = LottoOrder.objects.filter(province=province)
        self.city = list(set([x.city for x in self.db]))

    def main(self):
        city_data = [{'city_name':x, 'amount_all':AmountCity(x).all()} for x in self.city]
        return {'all': self.all(),'city': city_data}

    def sum_amount(self,db):
        return sum([x.amount for x in db])

    def all(self):
        return self.sum_amount(self.db)






def index(request):
    return render(request, 'index.html')

def welcome(request):

    # sell_data = {'all':12342413.00,'today':43434.00,'yestoday':'64546.00'}
    sell_data = AmountProvince('四川').main()
    return render(request, 'welcome.html',sell_data)

    [{
        time: '总数',
        totle: '425324534455'
    },
        {
            time: '今日',
            totle: '3144534'
        },
        {
            time: '本月',
            totle: '5423452345'
        },

    ]



# def order_list(request):
#     return render(request, 'order-list.html')
#
# def member_list(request):
#     return render(request, 'member-list.html')