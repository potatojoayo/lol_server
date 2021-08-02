from django.contrib import admin
from .models import Product,Category,Color,Size,Image,Brand


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Brand)

# Register your models here.
