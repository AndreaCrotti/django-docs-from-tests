import json

from django.shortcuts import render
from django.views.decorators.http import require_GET


# Create your views here.
@require_GET
def numbers(request, length=10):
    pass
