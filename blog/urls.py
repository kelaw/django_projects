from django.urls import path
from .views import (PostListVIew, PostDetailVIew, PostCreateView,
        PostUpdateView,
        PostDeleteView,
        UserPostListVIew)
from . import views

urlpatterns = [
    path('', PostListVIew.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListVIew.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailVIew.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-Create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]
