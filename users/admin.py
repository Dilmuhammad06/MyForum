from django.contrib import admin
from .models import User, Country

admin.site.register([User,Country])
