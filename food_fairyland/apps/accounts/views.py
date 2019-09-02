from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models import Count
from .forms import LoginForm, RegisterForm
from .models import User, Registeremail
import logging
import json
import re
import random
import string

logger = logging.getLogger('account')
# Create your views here.

class Login(View):
    # 当加载Login页面时
    # def get(self, request):
    #     # 如果已登录，则直接跳转到index页面
    #     # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
    #     # if request.user.is_authenticated:
    #     #     return redirect(reverse('fairyland:index'))
    #     form = LoginForm()
    #     return render(request, "index.html", {"form": form})

    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误!"}
        if request.is_ajax():
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                user, flag = form.check_password()
                if user and flag and user.is_active:
                    ret["status"] = 200
                    ret["msg"] = "登陆成功!"
                    auth.login(request, user)
                    logger.info(f"{user.username}登录成功")
                    return JsonResponse(ret, safe=False)
                ret["status"] = 201
                ret["msg"] = "用户名或密码错误!"
                print(ret["msg"])
                logger.error(f"{username}登录失败, {ret['msg']}")
            else:
                ret["status"] = 401
                ret["msg"] = "登陆表单数据不完整!"
                # logger.error(ret["msg"])
                print(ret["msg"])
                print(f"valid:{form.is_valid}")
                # my_error = form.errors
                # print(json.dumps(my_error))
                # print(json.loads(my_error))
        return JsonResponse(ret, safe=False)


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "index.html", {"form": form})

    def post(self, request):
        ret = {"status": 400, "msg": "调用方式错误!"}
        # print(request.get_host())
        # next = request.get_host()
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                if User.objects.filter(username=username).count() == 0:
                    password = form.cleaned_data["password"]
                    email = form.cleaned_data["email"]
                    email_captcha = form.cleaned_data["email_captcha"]
                    from django.core.cache import cache
                    email_captcha_reids = cache.get(email)
                    if email_captcha == email_captcha_reids:
                        user = User.objects.create(username=username, password=make_password(password), email=email)
                        user.save()
                        ret['status'] = 200
                        ret['msg'] = "注册成功!"
                        logger.debug(f"新用户{user}注册成功！")
                        user = auth.authenticate(username=username, password=password)
                        if user and user.is_active:
                            auth.login(request, user)
                            logger.debug(f"新用户{user}登录成功")
                        else:
                            logger.error(f"新用户{user}登录失败")
                    else:
                        # 验证码错误
                        ret['status'] = 401
                        ret['msg'] = "验证码错误或过期!"
                        logger.debug(f"用户注册结果：{ret}")
                else:
                    ret = {"status": 402, "msg": "用户名已存在!"}
                    logger.debug(f"用户注册结果：{ret}")
            else:
                ret['status'] = 405
                ret['msg'] = form.errors
                logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)



class Email_check(View):

    def post(self,request):
        email = request.POST.get("email")
        print(email)
        ret = {"status": 400, "msg": "调用方式错误"}
        # 已存在人数
        use_num = User.objects.filter(email=email).count()
        if use_num == 0:
            if re.match(r'^([\w]+\.*)([\w]+)\@[\w]+\.\w{3}(\.\w{2}|)$', email) is not None:
                email_code = "".join(random.choices(string.digits, k=4))
                from django.core.cache import cache
                cache.set(email, email_code, 300)
                send_mail('美食国度注册验证', f"您的验证码是：{email_code} ，如果您未在本网站提交注册验证，请忽略并删除此邮件。", None, [email])
                ret["status"] = 200
                ret["msg"] = "邮件发送成功，请登录邮箱查看！如果未找到可能在回收箱中。"
                return JsonResponse(ret, safe=False)
            else:
                ret["status"] = 404
                if email:
                    ret["msg"] = "输入的邮箱不合法！"
                    return JsonResponse(ret, safe=False)
                else:
                    ret["msg"] = "请输入邮箱号！"
                    return JsonResponse(ret, safe=False)
        else:
            ret["msg"] = "此邮箱已存在"
            return JsonResponse(ret, safe=False)



def logout(request):
    auth.logout(request)
    return redirect(reverse('fairyland:index'))