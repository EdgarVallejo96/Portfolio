from django.contrib import admin

from .models import Experience, Project


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "date_range", "order")
    list_editable = ("order",)
    ordering = ("order",)
    fieldsets = (
        ("English", {"fields": ("role", "company", "date_range", "description")}),
        ("Spanish (optional, falls back to English)", {"fields": ("role_es", "date_range_es", "description_es")}),
        ("Other", {"fields": ("technologies", "order")}),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "github_url", "order")
    list_editable = ("order",)
    ordering = ("order",)
    fieldsets = (
        ("English", {"fields": ("name", "description")}),
        ("Spanish (optional, falls back to English)", {"fields": ("description_es",)}),
        ("Other", {"fields": ("image", "technologies", "github_url", "demo_url", "order")}),
    )
