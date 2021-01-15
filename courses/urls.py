from django.urls import path

from courses.views import ManageCourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    CourseModuleUpdateView

urlpatterns = [
    path('mine/', ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('<pk>/module/', CourseModuleUpdateView.as_view(), name='course_module_update')
]
