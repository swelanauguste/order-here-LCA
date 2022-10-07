from django.contrib import admin

from .models import Category, District, Restaurant

admin.site.register(District)
admin.site.register(Category)
admin.site.register(Restaurant)
