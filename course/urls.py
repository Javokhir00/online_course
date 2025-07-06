from django.urls import path
from .views import *


app_name = 'course'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('subjects/<slug:slug>/', SubjectCoursesView.as_view(), name='subject_courses'),
    path('about/', AboutView.as_view(), name='about'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail') ,
    path('courses/<int:pk>/view/', CourseViewDetail.as_view(), name='course_view_detail'),

]