from django.urls import path
from django.views.decorators.http import require_POST
from .views import (
    PostListView,
    PostDetailedView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentFormView,
    CommentUpdateView,
    CommentDeleteView,
)
from . import views

app_name = "posts"

urlpatterns = [
    # posts urls
    path("", PostListView.as_view(), name="home"),
    path("user/<str:username>/posts", UserPostListView.as_view(), name="user-posts"),
    path("create/", PostCreateView.as_view(), name="create-post"),
    path("post/<pk>", PostDetailedView.as_view(), name="post"),
    path("post/<pk>/update", PostUpdateView.as_view(), name="update-post"),
    path("post/<pk>/delete", PostDeleteView.as_view(), name="delete-post"),
    path(
        "post/<pk>/comment",
        require_POST(CommentFormView.as_view()),
        name="create-post-comment",
    ),
    # comments urls
    path("comment/<pk>/update", CommentUpdateView.as_view(), name="update-comment"),
    path("comment/<pk>/delete", CommentDeleteView.as_view(), name="delete-comment"),
    # function based views
    path("about/", views.about, name="about"),
    path("vote/<int:pk>", views.vote, name="vote"),
]
