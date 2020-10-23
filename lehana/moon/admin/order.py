from django.contrib import admin
from moon.models.order import OrderItem, Order, Status, Invoice, Deliverer, ShippingAddress, Coupon
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Invoice)
admin.site.register(Deliverer)
admin.site.register(ShippingAddress)
admin.site.register(Coupon)
