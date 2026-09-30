from django.http import Http404
from django.templatetags.static import static
from django.shortcuts import render

from .i18n import UI_TEXT
from .models import Experience, Project


def home(request, lang):
    if lang not in UI_TEXT:
        raise Http404
    ui = UI_TEXT[lang]

    experiences = Experience.objects.all()
    for exp in experiences:
        exp.display_role = exp.localized_role(lang)
        exp.display_date_range = exp.localized_date_range(lang)
        exp.display_description_lines = exp.localized_description_lines(lang)

    projects = Project.objects.prefetch_related("photos").all()
    for project in projects:
        project.display_description = project.localized_description(lang)

    cv_file = "Edgar_Vallejo_CV_ES.pdf" if lang == "es" else "Edgar_Vallejo_CV_EN.pdf"

    context = {
        "lang": lang,
        "ui": ui,
        "experiences": experiences,
        "projects": projects,
        "cv_url": static(f"files/{cv_file}"),
    }
    return render(request, "portfolio/home.html", context)


def root(request):
    """Landing page at the site root; sends visitors to /en/ or /es/."""
    return render(request, "portfolio/root.html")
