from . views import HomeView, View_Post
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', View_Post.as_view(), name='post'),
]
