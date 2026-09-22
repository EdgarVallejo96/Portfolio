from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("lang/<str:lang_code>/", views.set_language, name="set_language"),
]
