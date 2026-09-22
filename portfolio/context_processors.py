from django.conf import settings


def site_links(request):
    return {
        "contact_email": settings.CONTACT_EMAIL,
        "github_url": settings.GITHUB_URL,
        "linkedin_url": settings.LINKEDIN_URL,
    }
