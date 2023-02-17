from django.http import HttpResponse

from . import settings


def sample_view(request):
    return HttpResponse(f"App version: {settings.APP_VERSION}")
