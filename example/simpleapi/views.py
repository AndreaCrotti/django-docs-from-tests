import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.http import require_GET


# Create your views here.
@require_GET
def numbers(request, length=10):
    result = json.dumps(list(range(length)))
    return HttpResponse(result)
