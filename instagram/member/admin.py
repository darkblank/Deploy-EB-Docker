from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from member.forms import UserForm
from member.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('nickname', 'img_profile', 'age', 'user_type', 'like_posts')}),
    )
    add_form = UserForm
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {'fields': ('nickname', 'img_profile', 'age', 'user_type')}),)


admin.site.register(User, UserAdmin)
