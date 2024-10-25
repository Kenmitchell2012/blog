from . views import HomeView, View_Post, CreateView, AddPost, UpdatePost, DeletePost, LikeView, AddCategoryView, CategoryView, CategoryListView, AddCommentView, DeleteCommentView, new_post_from_profile
from django.urls import include, path

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', View_Post.as_view(), name='post'),
    path('new_post/', AddPost.as_view(), name='new_post'),
    path('new_post_from_profile/', new_post_from_profile, name='new_post_from_profile'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='delete_post'),
    # path for liked posts
    path('like/<int:pk>', LikeView, name='like_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('<int:uid>/', include('members.urls')),
    # path for comments
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    # path('comment_list/<int:pk>', CommentListView.as_view(), name='comment_list'),
    # path('create_comment/<int:pk>', CreateCommentView.as_view(), name='create_comment'),
    # path('edit_comment/<int:pk>', EditCommentView.as_view(), name='edit_comment'),
    path('comment_delete/<int:pk>', DeleteCommentView, name='delete_comment'),
    # path('like_comment/<int:pk>', LikeCommentView.as_view(), name='like_comment'),
    # path('unlike_comment/<int:pk>', UnlikeCommentView.as_view(), name='unlike_comment'),


]
