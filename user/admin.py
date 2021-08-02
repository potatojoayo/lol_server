from django.contrib import admin
from .models import User,Address,Cart,Customer



# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'phone',
        'pcc',
        'birthday',
        'gender',
        'bank_account',
        
    ) 
    list_display_links = (
        'email',
        'name'
    )
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Customer)

