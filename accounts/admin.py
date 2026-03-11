from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_active",
            ),
        }),
    )
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    list_select_related = ("user",)
    search_fields = ("user__email", "first_name", "last_name")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)