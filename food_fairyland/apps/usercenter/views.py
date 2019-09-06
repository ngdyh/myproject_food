from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.contrib import auth
from django.http import JsonResponse
from apps.accounts.models import User
import logging
logger = logging.getLogger("account")


# Create your views here.

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'uc_window.html')
    def post(self,request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            if request.POST.get("email"):
                print('change email')
                request.user.email = request.POST.get("email")
            if request.POST.get("mobile"):
                print('change mobile')
                request.user.mobile = request.POST.get("mobile")
            if request.POST.get("qq"):
                request.user.qq = request.POST.get("qq")
            if request.POST.get("username"):
                print('change username')
                request.user.username = request.POST.get("username")
            request.user.save()
        except Exception as ex:
            ret_info = {"code": 400, "msg": "修改失败"}
        return render(request, 'uc_window.html', {"ret_info":ret_info})

class IntroView(LoginRequiredMixin, View):
    def post(self, request):
        ret_info = {"code": 400, "msg": "函数调用错误"}
        if request.is_ajax():
            ret_info = {"code": 200, "msg": "签名修改成功"}
            try:
                request.user.intro = request.POST.get("intro")
                request.user.save()
            except Exception as ex:
                ret_info = {"code": 401, "msg": "签名修改失败"}
        return JsonResponse(ret_info)

class ChangePasswdView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'uc_change_passwd.html')
    def post(self,request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            oldpassword = request.POST.get("oldpassword")
            newpassword1 = request.POST.get("newpassword1")
            newpassword2 = request.POST.get("newpassword2")
            print(oldpassword,newpassword1,newpassword2)
            if oldpassword and newpassword1 and newpassword2:
                if oldpassword != request.user.password:
                    if newpassword1 == newpassword2:
                        if oldpassword != newpassword1:
                            request.user.password = newpassword2
                            request.user.save()
                        else:
                            ret_info = {"code": 201, "msg": "新旧密码相同"}
                    else:
                        ret_info = {"code": 202, "msg": "新旧密码不一致"}
                else:
                    ret_info = {"code": 203, "msg": "密码错误"}
            else:
                ret_info = {"code": 204, "msg": "密码不能为空"}
        except Exception as ex:
            ret_info = {"code": 400, "msg": "修改失败"}
        return render(request, 'uc_change_passwd.html', {"ret_info":ret_info})