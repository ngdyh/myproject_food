"""authot:
   data:
"""

from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.hashers import check_password as auth_check_password

# 用户注册
class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="密 码2",max_length="128",
        widget=widgets.PasswordInput(attrs={"class": "password", "tabindex": "3", "placeholder": "请再次输入密码"}))
    email_captcha = forms.CharField(label="验证码", max_length="12", widget=widgets.TextInput(
        attrs={"placeholder": "验证码", "tabindex": "5", "error_messages": {"invalid": "验证码错误"}}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        # 自定义插件
        widgets = {
            'username': widgets.TextInput(attrs={"class": "name", "tabindex": "1", "placeholder": "请输入用户名"}),
            'email': widgets.TextInput(attrs={"class": "email col-lg-9", "style":"width: 70%;border-radius:2px 0 0 2px", "tabindex": "4", "placeholder": "请输入邮箱账号"}),
            'password': widgets.PasswordInput(attrs={"class": "password", "tabindex": "2",  "placeholder": "请输入密码"}),
        }

    # username是否重复django会自动检查，因为它是unique的，所以不需要自己写clean_username

    def clean_email(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("email"))
        if not ret:
            return self.cleaned_data.get("email")
        else:
            raise ValidationError("邮箱已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")



# 用户登陆
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length="32",
        widget=widgets.TextInput(attrs={"class": "name", "placeholder": "请输入用户名"}))
#     captcha = forms.CharField(label="验证码", widget=widgets.TextInput(
#         attrs={"style": "width: 160px;padding: 10px", "placeholder": "验证码", "onblur": "check_captcha()",
#                "error_messages": {"invalid": "验证码错误"}}))
    password = forms.CharField(label="密 码",max_length="128",
        widget=widgets.PasswordInput(attrs={"class": "password", "placeholder": "请输入密码"}))

    def check_password(self):
        print('check password')
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
            return user, auth_check_password(password, user.password)
        except:
            return None, False

    def clean_username(self):
        print(self.cleaned_data.get("username"))
        ret = User.objects.filter(username=self.cleaned_data.get("username"))
        if ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名或密码不正确")
