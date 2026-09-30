from django_distill import distill_path

from . import views
from .i18n import UI_TEXT

app_name = "portfolio"


def languages():
    return [{"lang": code} for code in UI_TEXT]


urlpatterns = [
    distill_path("", views.root, name="root", distill_file="index.html"),
    distill_path("<str:lang>/", views.home, name="home", distill_func=languages),
]
