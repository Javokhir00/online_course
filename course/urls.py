from django.urls import path
from .views import *
from .api_views import *

app_name = 'course'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('subjects/<slug:slug>/', SubjectCoursesView.as_view(), name='subject_courses'),
    path('about/', AboutView.as_view(), name='about'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail') ,
    path('courses/<int:pk>/view/', CourseViewDetail.as_view(), name='course_view_detail'),
    path('course-list/', CourseList.as_view(), name='course-list'),
    path('subject-list/', SubjectList.as_view(), name='subject-list'),
    path('subject-create/', SubjectCreate.as_view(), name='subject-create'),
    path('course-create/', CourseCreate.as_view(), name='course-create'),
    path('subject-detail/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('course-detail/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('course-update/<int:pk>/', CourseUpdate.as_view(), name='course-update'),
    path('course-delete/<int:pk>/', CourseDelete.as_view(), name='course-delete'),
    path('subject-update/<int:pk>/', SubjectUpdate.as_view(), name='subject-update'),
    path('subject-delete/<int:pk>/', SubjectDelete.as_view(), name='subject-delete'),

]