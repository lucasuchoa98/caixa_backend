from django.contrib import admin

# Register your models here.

from .models import Item, Venda

@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class ProductAdmin(admin.ModelAdmin):
    pass
