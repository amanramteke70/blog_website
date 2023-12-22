from django.contrib import admin
from .models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message')
admin.site.register(Contact,ContactAdmin)

class Blogadmin(admin.ModelAdmin):
    list_display = ('img','tittle', 'des')
admin.site.register(Blognews,Blogadmin)