from django.contrib import admin

from .models import Experience, Project


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "date_range", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "github_url", "order")
    list_editable = ("order",)
    ordering = ("order",)
