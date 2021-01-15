from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Course


def example(request):
    person = User.objects.get(pk=1)
    return HttpResponse(f"Hello world {getattr(person, 'username')}")


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'
