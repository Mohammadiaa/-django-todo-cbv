# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
# # Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = User

#     list_display = ("email", "first_name", "last_name", "is_staff", "is_active","updated_date")
#     list_filter = ("is_staff", "is_active", "is_superuser")
#     search_fields = ("email", "first_name", "last_name")
#     ordering = ("email",)

#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name")}),
#         ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
#     )

#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
#         }),
#     )

    

# admin.site.register(User, CustomUserAdmin)