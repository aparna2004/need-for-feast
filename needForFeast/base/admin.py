from django.contrib import admin
from .models import Items, Order, User

# Register your models here.
admin.site.register(Items)
admin.site.register(Order)
admin.site.register(User)

