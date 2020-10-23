from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from moon.models.product import Product, Brand, Maker, Look, Category, Variation, ItemVariation,ProductType


admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Maker)
admin.site.register(Look)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Variation)
admin.site.register(ItemVariation)
