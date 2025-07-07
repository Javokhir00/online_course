from django.urls import path, include
from .views import *
from .api_views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'course'

router = routers.DefaultRouter()
router.register(r'comments', CommentCrud, basename='comments')


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('subjects/<slug:slug>/', SubjectCoursesView.as_view(), name='subject_courses'),
    path('about/', AboutView.as_view(), name='about'),
    path('teachers/', TeacherView.as_view(), name='teachers'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail') ,
    path('courses/<int:pk>/view/', CourseViewDetail.as_view(), name='course_view_detail'),
    # path('comment-crud/', CommentCrud.as_view(), name='comment_crud'),          #-----------------------------
    path('', include(router.urls)),
    path('course-list/', CourseList.as_view(), name='course-list'),
    path('subject-list/', SubjectList.as_view(), name='subject-list'),
    path('subject-list-crud/<int:pk>/', SubjectListCrud.as_view(), name='subject-list_crud_list'),
    path('course-list-crud/<int:pk>/', CourseListCrud.as_view(), name='course-list_crud_list'),
    path('subject-create/', SubjectCreate.as_view(), name='subject-create'),
    path('course-create/', CourseCreate.as_view(), name='course-create'),
    path('subject-detail/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('course-detail/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('course-update/<int:pk>/', CourseUpdate.as_view(), name='course-update'),
    path('course-delete/<int:pk>/', CourseDelete.as_view(), name='course-delete'),
    path('subject-update/<int:pk>/', SubjectUpdate.as_view(), name='subject-update'),
    path('subject-delete/<int:pk>/', SubjectDelete.as_view(), name='subject-delete'),
    path('api/login/', obtain_auth_token, name='api_login'),
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),

]