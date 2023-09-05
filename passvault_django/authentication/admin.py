from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ["id", "email", "username", "name", "is_active", "is_premium", "is_admin", "email2", "username2", "created_at", "updated_at"]
    list_filter = ["is_active", "is_admin", "is_premium"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "username", "password"]}),
        ("Personal info", {"fields": ["name"]}),
        ("Permissions", {"fields": ["is_active", "is_premium", "is_admin"]}),
        ("Originals", {"fields": ["email2", "username2"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            "User Credentials", 
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"]
            }
        ),
        (
            "Personal info", 
            {
                "classes": ["wide"],
                "fields": ["name"]
            }
        ),
        (
            "Permissions", 
            {
                "classes": ["wide"],
                "fields": ["is_premium", "is_admin"]
            }
        ),
        (
            "Originals", 
            {
                "classes": ["wide"],
                "fields": ["email2", "username2"]
            }
        )
    ]
    search_fields = ["email", "username", "name"]
    ordering = ["email","id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)