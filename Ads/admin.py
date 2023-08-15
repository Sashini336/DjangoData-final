from django.contrib import admin
from .models import Ads, Image, Price

# Register your models here.



class AdsAdmin(admin.ModelAdmin):
    list_filter = ['title', 'year', 'fuel_type', 'price',]

admin.site.register(Ads, AdsAdmin)

admin.site.register(Image)

admin.site.register(Price)

