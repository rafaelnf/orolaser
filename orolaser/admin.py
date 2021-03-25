# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *



class BannerAdmin(admin.ModelAdmin):
    list_display = ['name','photo','price', 'oroClub']

    search_fields = ['name',]
admin.site.register(Banner,BannerAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ['name','photo','address', 'lat', 'long', 'opening_hours']


    search_fields = ['name',]
admin.site.register(Units,UnitAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['message',]


    search_fields = ['message',]
admin.site.register(Notification,NotificationAdmin)

class TokenAdmin(admin.ModelAdmin):
    list_display = ['token',]


    search_fields = ['token',]
admin.site.register(Token,TokenAdmin)