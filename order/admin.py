from django.contrib import admin
from .models import Order,OrderStatus,OrderedProduct

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderedProduct)

