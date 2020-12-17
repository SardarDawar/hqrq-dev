from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'date_joined', 'groups')}),
        ('Permissions', {'fields': ('user_permissions', 'is_staff', 'is_active', 'is_superuser')}),
        ('Profile', {'fields': ('image', 'email_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'email_verified', 'first_name', 'last_name')}
        ),
    )
    search_fields = ('email',)
    ordering = ('date_joined',)

    def full_name(self, obj):
        return obj.get_full_name()
    
    full_name.short_description = 'Full Name'

admin.site.register(CustomUser, CustomUserAdmin)