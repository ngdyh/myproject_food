from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic import View
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from apps.accounts.forms import LoginForm, RegisterForm
from apps.accounts.models import User
from . import models
import logging

# Create your views here.
# logger = logging.getLogger('account')

# 包含注册/登陆


def index(request):
    register_form = RegisterForm()
    login_form = LoginForm()

    return render(request, 'index.html', {"login_form": login_form, 'register_form': register_form})

    # # Ajax提交表单
    # def post(self, request):
    #     from django.core.cache import cache
    #     ret = {"status": 400, "msg": "调用方式错误"}
    #     if request.is_ajax():
    #         form_register = RegisterForm(request.POST)
    #         form_login = LoginForm(request.POST)
    #         keys = request.POST.get('keys')
    #         # 注册
    #         if keys == "2":
    #             if form_register.is_valid():
    #                 username = form_register.cleaned_data["username"]
    #                 password = form_register.cleaned_data["password"]
    #                 email = form_register.cleaned_data["email"]
    #                 # email_captcha = form_register.cleaned_data["email_captcha"]
    #                 # email_captcha_reids = cache.get(email)
    #                 # if email_captcha == email_captcha_reids:
    #                 user = User.objects.create(username=username, password=make_password(password), email=email)
    #                 user.save()
    #                 ret['status'] = 200
    #                 ret['msg'] = "注册成功"
    #                 logger.debug(f"新用户{user}注册成功！")
    #                 user = auth.authenticate(username=username, password=password)
    #                 if user and user.is_active:
    #                     auth.login(request, user)
    #                     logger.debug(f"新用户{user}登录成功")
    #                 else:
    #                     logger.error(f"新用户{user}登录失败")
    #                 # else:
    #                 #     # 验证码错误
    #                 #     ret['status'] = 401
    #                 #     ret['msg'] = "验证码错误或过期"
    #                 logger.debug(f"用户注册结果：{ret}")
    #             else:
    #                 ret['status'] = 402
    #                 ret['msg'] = form_register.errors
    #                 logger.debug(f"用户注册结果：{ret}")
    #
    #         # 登陆
    #         elif keys == "1":
    #             if form_login.is_valid():
    #                 username = form_login.cleaned_data["username"]
    #                 user, flag = form_login.check_password()
    #                 if user and flag and user.is_active:
    #                     auth.login(request, user)
    #                     logger.info(f"{user.username}登录成功")
    #                     return redirect(request.session.get('/'))
    #                 msg = "用户名或密码错误"
    #                 print(msg)
    #                 logger.error(f"{username}登录失败, {msg}")
    #                 return render(request, "index.html", {"form": form_login, "msg": msg})
    #             else:
    #                 msg = "登陆表单数据不完整"
    #                 logger.error(msg)
    #                 print(msg)
    #                 # return redirect(request.session.get('/'),{"form": form_login, "msg": msg})
    #                 return JsonResponse({"msg": msg})
    #         elif keys == "0" or not keys:
    #             logger.error("keys值为空或0")
    #             print("keys值空")
    #         else:
    #             logger.error(f"错误，keys值为{keys}")
    #             print(f"错误，keys值为{keys}")
    #     return JsonResponse(ret)



class Dishes_search(View):
    def get(self, request, id1, id2, id3, id4):
        try:
            if id1.isdigit and id2.isdigit and id3.isdigit and id4.isdigit:
                if 0 <= int(id1) <= 1 and 0 <= int(id2) <=5 and 0 <= int(id3) <= 3 and 0 <= int(id2) <= 4:
                    country = ""
                    if id1 == "1":
                        country = "国外"
                        dish = models.Dish.objects.all().filter(genre=2)
                    elif id1 == "0":
                        country = "国内"
                        dish = models.Dish.objects.all().filter(genre=1)

                        category1 = models.Category.objects.filter(name='正餐主食')
                        category2 = models.Category.objects.filter(name='甜品小吃')
                        category3 = models.Category.objects.filter(name='时尚饮品')
                        category4 = models.Category.objects.filter(name='鲜汤粥类')
                        category5 = models.Category.objects.filter(name='秘制酱料')
                        if id2 == 0:
                            pass
                        elif id2 == 1:
                            dish = dish.filter(category=category1)
                        elif id2 == 2:
                            dish = dish.filter(category=category2)
                        elif id2 == 3:
                            dish = dish.filter(category=category3)
                        elif id2 == 4:
                            dish = dish.filter(category=category4)
                        elif id2 == 5:
                            dish = dish.filter(category=category5)

                        district1 = models.District.objects.filter(name="鲁菜")
                        district2 = models.District.objects.filter(name="湘菜")
                        district3 = models.District.objects.filter(name="未分类")
                        if id3 == 0:
                            pass
                        elif id3 == 1:
                            dish = dish.filter(district=district1)
                        elif id3 == 2:
                            dish = dish.filter(district=district2)
                        elif id3 == 3:
                            dish = dish.filter(district=district3)


                        meal1 = models.Meal.objects.filter(name="早餐")
                        meal2 = models.Meal.objects.filter(name="午餐")
                        meal3 = models.Meal.objects.filter(name="下午茶")
                        meal4 = models.Meal.objects.filter(name="晚餐")
                        if id4 == 0:
                            pass
                        elif id4 == 1:
                            dish = dish.filter(meal=meal1)
                        elif id4 == 2:
                            dish = dish.filter(meal=meal2)
                        elif id4 == 3:
                            dish = dish.filter(meal=meal3)
                        elif id4 == 4:
                            dish = dish.filter(meal=meal4)

                    return render(request, 'dishes_search.html', {'dish': dish, 'country': country})
                else:
                    raise ValueError("值域不存在")
            else:
                raise TypeError("参数错误")
        except Exception as ex:
            print(ex)
        return HttpResponse('404')

