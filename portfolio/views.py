from django.shortcuts import render

from .models import Experience, Project


def home(request):
    context = {
        "experiences": Experience.objects.all(),
        "projects": Project.objects.all(),
    }
    return render(request, "portfolio/home.html", context)
