from django.contrib import admin

# Register your models here.

from base_model import models

admin.site.register(models.User)
admin.site.register(models.Agent)
admin.site.register(models.LottoOrder)
admin.site.register(models.UserRecommend)