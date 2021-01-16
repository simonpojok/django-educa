from django.urls import path

from students.views import StudentRegistrationView, StudentEnrollCourseView

urlpatterns = [
    path('register/', StudentRegistrationView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course')
]
