from django.db import models

# Create your models here.

class User(models.Model):

    uid = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    username = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=32,null=True,blank=True)
    wx_nickname = models.CharField(max_length=255,null=True,blank=True)
    wx_name = models.CharField(max_length=255,null=True,blank=True)
    wx_sex = models.IntegerField(null=True,blank=True)
    wx_city = models.CharField(max_length=255,null=True,blank=True)
    wx_province = models.CharField(max_length=255,null=True,blank=True)
    wx_avatar = models.CharField(max_length=255,null=True,blank=True)
    wx_id = models.CharField(max_length=255,null=True,blank=True)
    mobile = models.CharField(max_length=11,null=True,blank=True)
    id_card = models.CharField(max_length=30,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    bank_account = models.CharField(max_length=30,null=True,blank=True)
    auth_key = models.CharField(max_length=32,null=True,blank=True)
    access_token = models.CharField(max_length=100,null=True,blank=True)
    province = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    provcode = models.CharField(max_length=10,null=True,blank=True)
    citycode = models.CharField(max_length=10,null=True,blank=True)
    role = models.IntegerField(
        choices=((0,'普通用户'),(1,'省'),(2,'市'),(3,'管理员'),
                 (4,'一级代理'),(5,'二级代理')
                 ),
                 default=0
    )
    status = models.IntegerField(
        choices=((0,'正常'),(1,'不正常')),
                 default=0
    )
    created = models.IntegerField(null=True,blank=True)
    changed = models.IntegerField(null=True,blank=True)


    def __str__(self):
        return str(self.uid)


class Agent(models.Model):
    uid = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)


class UserRecommend(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField(null=True,blank=True)
    p1 = models.IntegerField(null=True,blank=True)
    p2 = models.IntegerField(null=True,blank=True)
    p3 = models.IntegerField(null=True,blank=True)
    p4 = models.IntegerField(null=True,blank=True)


class LottoOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100,null=True,blank=True)
    uid = models.IntegerField(null=True,blank=True)
    lotto_id = models.CharField(unique=True,max_length=10,null=True,blank=True)
    issue = models.CharField(max_length=20,null=True,blank=True)
    multiple = models.IntegerField(null=True,blank=True)
    follow = models.IntegerField(default=1)
    payment = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=11, decimal_places=2,null=True,blank=True)
    status = models.IntegerField(default=-1)
    province = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    created = models.IntegerField(null=True,blank=True)
    changed = models.IntegerField(null=True,blank=True)

    # amount的总额 省份 时间  province  city
    # 排名


