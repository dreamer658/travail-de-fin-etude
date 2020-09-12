from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from moon.models.product import Product,Shoes, Clothes, Accessory, Brand, Maker, Look, Category

admin.site.register(Product)
admin.site.register(Shoes)
admin.site.register(Clothes)
admin.site.register(Accessory)
admin.site.register(Brand)
admin.site.register(Maker)
admin.site.register(Look)
admin.site.register(Category, MPTTModelAdmin)
