from django.contrib.auth.views import LogoutView
from . views import UserRegisterView
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
