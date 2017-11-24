import random,time
from datetime import datetime


class AmountCommon():
    def __init__(self,db):
        self.db = db

    def sum_amount(self, db):
        return sum([x.amount for x in db])

    def all(self):
        return str(self.sum_amount(self.db))

    def today(self):
        t = time.localtime(time.time())
        time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t),
                                          '%Y-%m-%d %H:%M:%S'))

        today_zero = int(time1)
        now = int(time.time())
        tdb = self.db.filter(created__range=(today_zero, now))
        return str(self.sum_amount(tdb))

    def this_month(self):
        d = datetime.now()
        b = '{0}-{1}-1 00:00:00'.format(d.year, d.month)
        month_zero = int(time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S")))
        now = int(time.time())
        tdb = self.db.filter(created__range=(month_zero, now))
        return str(self.sum_amount(tdb))


    def time_formater(self,year,month,day):
        b = '{0}-{1}-{2} 00:00:00'.format(year, month, day)
        month_zero = int(time.mktime(time.strptime(b, "%Y-%m-%d %H:%M:%S")))

        return month_zero

    def time_range(self,last,now):
        tlast = self.time_formater(last[0], last[1], last[2])
        tnow = self.time_formater(now[0], now[1], now[2])
        tdb = self.db.filter(created__range=(tlast, tnow))
        return str(self.sum_amount(tdb))