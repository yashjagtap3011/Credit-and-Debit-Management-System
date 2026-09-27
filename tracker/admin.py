from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Transaction, Tutorial

# Replace Django's default User registration with this expanded admin list.
admin.site.unregister(User)

# Administrators can quickly review account status, staff access, and sign-ins.
@admin.register(User)
class TrackerUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "last_login",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date", "user", "transaction_type", "category", "amount")
    list_filter = ("transaction_type", "category", "date")
    search_fields = ("user__username", "description", "category")


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "created_by", "updated_at")
    list_filter = ("is_published", "category")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}
