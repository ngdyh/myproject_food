from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name="手机号")
    intro = models.TextField(max_length=128, default="此用户太懒，暂无签名~", verbose_name="个性签名")
    qq = models.CharField(max_length=15, verbose_name="QQ号")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name



class Registeremail(models.Model):
    verify_code = models.CharField(max_length=128, verbose_name="验证码")
    email = models.EmailField(verbose_name="邮箱")
    creat_time = models.DateTimeField(auto_now=True, verbose_name="重置时间")
    status = models.BooleanField(default=False, verbose_name="是否已重置")

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name