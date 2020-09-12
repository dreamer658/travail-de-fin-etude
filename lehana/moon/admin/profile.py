from django.contrib import admin
from moon.models.profile import UserProfile, Favorite, Comment, Discount

admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Discount)
