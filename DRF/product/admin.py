from django.contrib import admin
from .models import Category , Product ,ProductDetail, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductDetail)

