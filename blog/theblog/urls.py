from . views import HomeView, View_Post, CreateView, AddPost
from django.urls import path

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', View_Post.as_view(), name='post'),
    path('new_post/', AddPost.as_view(), name='new_post'),
]
