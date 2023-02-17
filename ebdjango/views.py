from django.http import HttpResponse


def sample_view(request):
    return HttpResponse("App version: 1.0.0")