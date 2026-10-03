from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ClientProfile, Department, EmployeeProfile, Team, User


# USER ADMIN =====================
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "full_name",
        "role",
        "is_online",
        "is_active",
        "date_joined",
        "last_seen",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_online",
        "date_joined",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone",
    )

    ordering = ("-date_joined",)
    readonly_fields = (
        "last_login",
        "date_joined",
        "last_seen",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "TeamCore Information",
            {
                "fields": (
                    "role",
                    "phone",
                    "avatar",
                    "is_online",
                    "last_seen",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "TeamCore Information",
            {
                "fields": (
                    "email",
                    "role",
                    "phone",
                    "avatar",
                )
            },
        ),
    )

    @admin.display(description="Full Name")
    def full_name(self, obj):
        return obj.get_full_name() or "-"


# DEPARTMENT ADMIN ====================
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "head",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
        "description",
    )

    autocomplete_fields = ("head",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("name",)


# TEAM ADMIN ====================
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "department",
        "team_lead",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "department",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
        "department__name",
        "team_lead__username",
        "team_lead__first_name",
        "team_lead__last_name",
    )

    autocomplete_fields = (
        "department",
        "team_lead",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("name",)


# EMPLOYEE PROFILE ADMIN ===================
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "user",
        "department",
        "team",
        "designation",
        "manager",
        "employment_type",
        "joining_date",
        "is_active_employee",
    )

    list_filter = (
        "department",
        "team",
        "employment_type",
        "is_active_employee",
        "joining_date",
    )

    search_fields = (
        "employee_id",
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
        "designation",
    )

    autocomplete_fields = (
        "user",
        "department",
        "team",
        "manager",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("employee_id",)


# CLIENT PROFILE ADMIN ===================
@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "company_code",
        "contact_person",
        "phone",
        "user",
        "is_active_client",
        "created_at",
    )

    list_filter = (
        "is_active_client",
        "created_at",
    )

    search_fields = (
        "company_name",
        "company_code",
        "contact_person",
        "phone",
        "user__username",
        "user__email",
    )

    autocomplete_fields = ("user",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("company_name",)
