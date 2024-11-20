from django.contrib import admin
from .models import Category, Tread, Post


admin.site.register([Category,Tread,Post])
