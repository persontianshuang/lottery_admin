def new_lo():
        lo = LottoOrder()
        lo.amount = random.randint(1, 5000)
        lo.province = '四川'
        lo.city = '绵阳'
        lo.created = random.choice(range(1503635719,1511148621))
        print(lo.amount)
        lo.save()
    [new_lo() for x in range(1000)]

    for l in LottoOrder.objects.all():
        # l.created = random.choice(range(1503635719,1511148621))
        l.uid = str(random.choice(range(30,110)))
        l.save()

    for u in User.objects.all():
        str_nums = 'qwertyuipasdfgjklzxcvbnm'
        u.name = ''.join([random.choice(str_nums) for _ in range(11)])
        u.save()

    def new_user():
        str_nums = '123456789'
        user = User()
        user.username = ''.join([random.choice(str_nums) for _ in range(11)])
        user.mobile = user.username
        user.pasword = 13333333333
        user.role = random.choice([4,5])
        user.save()
    [new_user() for _ in range(100)]


    print(self.alldb)