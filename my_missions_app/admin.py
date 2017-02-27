from .models import *
from django.contrib import admin
#from .forms import AdminUserChangeForm, AdminUserAddForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

'''
class CustomUserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar',
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'phone', 'password1', 'password2')}
        ),
    )
'''


class CustomUserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'phone',
        'avatar',
        'last_cat',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'user_id',
    )


class MissionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'comment',
        'cat_id',
        'until_datetime',
        'remind_datetime',
    )


class RemindLoopAdmin(admin.ModelAdmin):
    list_display = (
        'mission',
        'day',
    )


class WeekDaysAdmin(admin.ModelAdmin):
    list_display = (
        'day_id',
        'name',
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Missions, MissionsAdmin)
admin.site.register(RemindLoop, RemindLoopAdmin)
admin.site.register(WeekDays, WeekDaysAdmin)