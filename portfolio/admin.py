from django.contrib import admin

from .models import Experience, Project, ProjectImage


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


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "github_url", "order")
    list_editable = ("order",)
    ordering = ("order",)
    inlines = [ProjectImageInline]
    fieldsets = (
        ("English", {"fields": ("name", "description")}),
        ("Spanish (optional, falls back to English)", {"fields": ("description_es",)}),
        (
            "Photo",
            {
                "fields": ("image",),
                "description": (
                    "Use this for a single screenshot. To upload multiple photos with left/right "
                    "navigation on the site, add them in the 'Project images' section below instead — "
                    "those take priority over this field when present."
                ),
            },
        ),
        ("Other", {"fields": ("technologies", "github_url", "demo_url", "order")}),
    )
