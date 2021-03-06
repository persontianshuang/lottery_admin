"""lottery_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import TemplateView

from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    url(r'^province/', include('province.urls')),
    url(r'^city/', include('city.urls')),
    url(r'^agent1/', include('agent1.urls')),
    url(r'^agent2/', include('agent2.urls')),
    url(r'^login/', include('login.urls')),
]
