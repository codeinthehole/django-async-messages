from django.template.response import TemplateResponse
from django.template import Template


def index(request):
    t = Template("")
    return TemplateResponse(request, t, {'a': 1000})
