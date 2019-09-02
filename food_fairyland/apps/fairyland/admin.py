from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Meal)
admin.site.register(models.Category)
admin.site.register(models.District)
admin.site.register(models.Dish)
admin.site.register(models.Comment)