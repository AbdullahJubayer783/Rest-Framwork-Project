from django.contrib import admin
from . import models
# Register your models here.
class ColorCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    
admin.site.register(models.ColorCategoryModel,ColorCatAdmin)

class FlowerCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.register(models.FlowerCategoryModel,FlowerCatAdmin)

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['title','quantity','price']

admin.site.register(models.FlowerModel,FlowerAdmin)

admin.site.register(models.ReviewModel)
