from django.conf import settings

from .i18n import UI_TEXT


def site_links(request):
    return {
        "contact_email": settings.CONTACT_EMAIL,
        "github_url": settings.GITHUB_URL,
        "linkedin_url": settings.LINKEDIN_URL,
    }


def site_language(request):
    lang = request.session.get("lang", "en")
    if lang not in UI_TEXT:
        lang = "en"
    return {
        "lang": lang,
        "ui": UI_TEXT[lang],
    }
