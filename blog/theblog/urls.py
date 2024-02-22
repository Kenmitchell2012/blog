from . views import HomeView, View_Post, CreateView, AddPost, UpdatePost, DeletePost, LikeView, AddCategoryView, CategoryView, CategoryListView
from django.urls import include, path

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', View_Post.as_view(), name='post'),
    path('new_post/', AddPost.as_view(), name='new_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='delete_post'),
    #path for liked posts
    path('like/<int:pk>', LikeView, name='like_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('<int:uid>/', include('members.urls'))


]
