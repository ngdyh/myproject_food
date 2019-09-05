from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from apps.accounts.models import User
# Create your models here.

# 能否为空，默认值




class Meal(models.Model):
    """所有用餐时间"""
    name = models.CharField(verbose_name="分段时间名",max_length=64)

    class Meta:
        verbose_name = "分段时间"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"




class Category(models.Model):
    """菜品分类"""
    name = models.CharField(verbose_name="分类名称", max_length=64)

    class Meta:
        verbose_name = "食物分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"



class District(models.Model):
    """地区菜式"""
    name = models.CharField(verbose_name="地区菜名",max_length=64)

    class Meta:
        verbose_name = "地区菜式"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"






class Dish(models.Model):
    """菜品"""

    IN_OUT_COUNTRY = ((1, "国内"), (2, "国外"))

    name = models.CharField(verbose_name="菜品名", max_length=64)
    inro = RichTextUploadingField(verbose_name="菜品介绍", max_length=1024)
    produce =RichTextUploadingField(verbose_name="制作方法", max_length=1024)
    genre = models.IntegerField(verbose_name="国内外", choices=IN_OUT_COUNTRY)
    category = models.ForeignKey(Category, verbose_name="菜品分类")
    district = models.ForeignKey(District, verbose_name="地区菜式")
    meal = models.ManyToManyField(Meal, verbose_name="适合时间")
    img_sm = models.ImageField(verbose_name="菜品小图", upload_to="avator/dishes_thumb/", default="avator/img_sm_404.jpg")
    img = models.ImageField(verbose_name="菜品大图", upload_to="avator/dishes/", default="avator/img_404.jpg")

    class Meta:
        verbose_name = "所有菜品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"



class Comment(models.Model):
    """评论"""
    user = models.ForeignKey(User, verbose_name="评论者")
    obj = models.ForeignKey(Dish, verbose_name="评论对象")
    content = RichTextUploadingField(verbose_name="评论内容", max_length=128)
    comment_time = models.DateTimeField(verbose_name="评论时间", auto_now_add=True)


    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user}"