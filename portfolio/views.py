from django.http import HttpResponseRedirect
from django.templatetags.static import static
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.shortcuts import render

from .i18n import UI_TEXT
from .models import Experience, Project


def home(request):
    lang = request.session.get("lang", "en")
    if lang not in UI_TEXT:
        lang = "en"

    experiences = Experience.objects.all()
    for exp in experiences:
        exp.display_role = exp.localized_role(lang)
        exp.display_date_range = exp.localized_date_range(lang)
        exp.display_description_lines = exp.localized_description_lines(lang)

    projects = Project.objects.all()
    for project in projects:
        project.display_description = project.localized_description(lang)

    cv_file = "Edgar_Vallejo_CV_ES.pdf" if lang == "es" else "Edgar_Vallejo_CV_EN.pdf"

    context = {
        "experiences": experiences,
        "projects": projects,
        "cv_url": static(f"files/{cv_file}"),
    }
    return render(request, "portfolio/home.html", context)


def set_language(request, lang_code):
    if lang_code not in UI_TEXT:
        lang_code = "en"
    request.session["lang"] = lang_code

    next_url = request.GET.get("next")
    if not (next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()})):
        next_url = reverse("portfolio:home")
    return HttpResponseRedirect(next_url)
