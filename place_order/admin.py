from django.contrib import admin
from . import models

# Register your models here.
class OderAdmin(admin.ModelAdmin):
    list_display = ['who_orderd','flower_title','quantity','order_status','date']
    def who_orderd(self,obj):
        return obj.user.user.first_name
    def flower_title(self,obj):
        return obj.flower.title

admin.site.register(models.OrderDetails,OderAdmin)