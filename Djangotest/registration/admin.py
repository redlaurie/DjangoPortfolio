from django.contrib import admin
from .models import Profile,Order,OrderItem,ShippingAddress,Product

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)