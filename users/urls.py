from django.urls import path , include
from .views import Login , Register , activate_account, LogOut


app_name = 'users'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('logout/', LogOut.as_view(), name='logout'),

]