from django.forms import inlineformset_factory

from courses.models import Course, Module

ModuleFormSet = inlineformset_factory(
    Course,
    Module,
    fields=['title', 'description'],
    extra=1,
    can_delete=True,
)

