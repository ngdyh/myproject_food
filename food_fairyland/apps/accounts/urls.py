"""authot:
   data:
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views




urlpatterns = [
    # 登陆
    url(r'^login/$', views.Login.as_view(), name='login'),
    # 注册
    url(r'^register/$', views.Register.as_view(), name='register'),
    # 注册邮箱验证
    url(r'^register/email_check$', views.Email_check.as_view(),name="email_check"),
    # 注销
    url(r'^logout/$', views.logout, name="logout"),

]
