from django.db import models

# Create your models here.

class ProvinceSorted(models.Model):
    province = models.CharField(max_length=100,null=True,blank=True)
    rank = models.IntegerField(null=True,blank=True)
    amount_sum = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    add_time = models.IntegerField(null=True,blank=True)