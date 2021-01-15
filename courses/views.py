from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def example(request):
    person = User.objects.get(pk=1)
    return HttpResponse(f"Hello world {getattr(person, 'username')}")
