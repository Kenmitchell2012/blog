from django.contrib.auth.views import LogoutView
from . views import UserRegisterView, UserEditView
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
