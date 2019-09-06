"""authot:
   data:
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    # 个人中心
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    # 个性签名
    url(r'^intro/$', views.IntroView.as_view(), name='intro'),
    # 修改密码
    url(r'^change_passwd/$', views.ChangePasswdView.as_view(), name='change_passwd'),


]
