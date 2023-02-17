from django.http import HttpResponse

from ebdjango.ebdjango import settings


def sample_view(request):
    return HttpResponse(f"App version: {settings.APP_VERSION}")
