from django.http import HttpResponse

from . import settings


def sample_view(request):
    return HttpResponse(f"App Version: {settings.APP_VERSION}")
