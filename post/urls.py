from django.urls import path
from .views import CreatePostView, ListPostsView,PostAPIView

urlpatterns = [
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
    path('posts/api/', ListPostsView.as_view(), name='list_posts_api'),
    path('posts/api/<int:prace_id>/', PostAPIView.as_view(), name='post-api'),
]
