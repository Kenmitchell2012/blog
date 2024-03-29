from django.contrib.auth.views import LogoutView
from . views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:uid>/password/', PasswordsChangeView.as_view(),name='password'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password'),
    # path('<int:uid>/password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='password'),
    path('password_success/', views.password_success, name='password_success'),
    # profile page
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),


]
