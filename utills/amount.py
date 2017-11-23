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