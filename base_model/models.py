from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    # 用户的唯一标识
    uid = models.AutoField(primary_key=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)


    # 微信相关
    wx_nickname = models.CharField(max_length=255,null=True,blank=True)
    wx_name = models.CharField(max_length=255,null=True,blank=True)
    wx_sex = models.IntegerField(null=True,blank=True)
    wx_city = models.CharField(max_length=255,null=True,blank=True)
    wx_province = models.CharField(max_length=255,null=True,blank=True)
    wx_avatar = models.CharField(max_length=255,null=True,blank=True)
    wx_id = models.CharField(max_length=255,null=True,blank=True)

    # username在django中必须要唯一，所以username和mobile都用手机号来表示
    # 用name来表示昵称
    username = models.CharField(max_length=100,unique=True)
    mobile = models.CharField(max_length=11,unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    # password = models.CharField(max_length=32,null=False)

    id_card = models.CharField(max_length=30,null=True,blank=True)
    bank_name = models.CharField(max_length=100,null=True,blank=True)
    bank_account = models.CharField(max_length=30,null=True,blank=True)
    # 推广页面标识
    auth_key = models.CharField(max_length=32,null=True,blank=True)
    access_token = models.CharField(max_length=100,null=True,blank=True)
    # 一级代理,省，市都是分配
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
    # 二级代理 可为空，因为可以通过一级代理直接购票
    p1 = models.IntegerField(null=True,blank=True)
    # 一级代理，计算总额时，不用累加二级代理的值
    p2 = models.IntegerField(null=True,blank=True)
    # 不用管下面的，是通过手机号来的
    # 市
    p3 = models.IntegerField(null=True,blank=True)
    # 省
    p4 = models.IntegerField(null=True,blank=True)

    uid_user = models.ForeignKey(User, null=True, blank=True)
    # 原表基础上增加
    created = models.IntegerField(null=True, blank=True)


class LottoOrder(models.Model):
    # 用户标识
    uid = models.IntegerField(null=True, blank=True)

    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100,null=True,blank=True)

    lotto_id = models.CharField(unique=True,max_length=10,null=True,blank=True)
    issue = models.CharField(max_length=20,null=True,blank=True)
    multiple = models.IntegerField(null=True,blank=True)
    follow = models.IntegerField(default=1)
    payment = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=11, decimal_places=2,null=True,blank=True)
    status = models.IntegerField(default=-1)

    province = models.CharField(max_length=100 , null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    created = models.IntegerField(null=True,blank=True)
    changed = models.IntegerField(null=True,blank=True)

    # 原表基础上增加
    from_agent = models.ForeignKey(UserRecommend,null=True,blank=True)

    # amount的总额 省份 时间  province  city
    # 排名

#     代理1





