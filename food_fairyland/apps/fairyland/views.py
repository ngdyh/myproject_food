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



class Dishes_search(View):
    def get(self, request, id1, id2, id3, id4):
        register_form = RegisterForm()
        login_form = LoginForm()
        try:
            if id1.isdigit and id2.isdigit and id3.isdigit and id4.isdigit:

                if 0 <= int(id1) <= 1 and 0 <= int(id2) <= 5 and 0 <= int(id3) <= 4 and 0 <= int(id4) <= 4:
                    country = ""
                    if id1 == "1":
                        country = "国外"
                        dishes = models.Dish.objects.all().filter(genre=2)
                        if id2 != "0":
                            dict_category = {"1": "正餐主食", "2": "甜品小吃", "3": "时尚饮品", "4": "鲜汤粥类", "5": "秘制酱料"}
                            category = models.Category.objects.filter(name=dict_category[id2])
                            dishes = dishes.filter(category=category)
                        if id3 != "0":
                            dict_district = {"1": "美式", "2": "日式", "3": "英式", "4": "意式"}
                            district = models.District.objects.filter(name=dict_district[id3])
                            dishes = dishes.filter(district=district)
                        if id4 != "0":
                            dict_meal = {"1": "早餐", "2": "午餐", "3": "下午茶", "4": "晚餐"}
                            meal = models.Meal.objects.filter(name=dict_meal[id4])
                            dishes = dishes.filter(meal=meal)
                    elif id1 == "0":
                        country = "国内"
                        dishes = models.Dish.objects.all().filter(genre=1)
                        if id2 != "0":
                            dict_category = {"1": "正餐主食", "2": "甜品小吃", "3": "时尚饮品", "4": "鲜汤粥类", "5": "秘制酱料"}
                            category = models.Category.objects.filter(name=dict_category[id2])
                            dishes = dishes.filter(category=category)

                        if id3 != "0":
                            dict_district = {"1": "鲁菜", "2": "湘菜", "3": "未分类"}
                            district = models.District.objects.filter(name=dict_district[id3])
                            dishes = dishes.filter(district=district)

                        if id4 != "0":
                            dict_meal = {"1": "早餐", "2": "午餐", "3": "下午茶", "4": "晚餐"}
                            meal = models.Meal.objects.filter(name=dict_meal[id4])
                            dishes = dishes.filter(meal=meal)

                    return render(request, 'dishes_search.html', {'dishes': dishes, 'country': country, "login_form": login_form, 'register_form': register_form})
                else:
                    raise ValueError("值域不存在")
            else:
                raise TypeError("参数错误")
        except Exception as ex:
            print(ex)
        return HttpResponse('404')


class Dishes(View):
    def get(self, request, id):
        register_form = RegisterForm()
        login_form = LoginForm()
        dish = models.Dish.objects.get(id=id)

        return render(request, 'dishes.html', {"login_form": login_form, 'register_form': register_form, 'dish': dish})
