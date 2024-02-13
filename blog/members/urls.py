from . views import UserRegisterView
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
