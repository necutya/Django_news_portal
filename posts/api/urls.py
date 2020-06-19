from django.urls import path

from .views import (
    PosListApiView,
    PostDetailApiView,
    PostCreateApiView,
    PostUpdateApiView,
    PostDeleteApiView,
    PostVoteApiView,
    CommentListApiView,
    CommentDetailApiView,
    CommentCreateApiView,
    CommentUpdateApiView,
    CommentDeleteApiView,
)

app_name = "posts-api"
urlpatterns = [
    # API for posts
    path("posts/", PosListApiView.as_view(), name="posts"),
    path("posts/<int:pk>/", PostDetailApiView.as_view(), name="post"),
    path("posts/create/", PostCreateApiView.as_view(), name="post-create"),
    path("posts/<int:pk>/update/", PostUpdateApiView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteApiView.as_view(), name="post-delete"),
    # Vote-post API
    path("posts/<int:pk>/vote/", PostVoteApiView.as_view(), name="post-vote"),
    # API for comments
    path("comments/", CommentListApiView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetailApiView.as_view(), name="comment"),
    path("comments/create/", CommentCreateApiView.as_view(), name="comment-create"),
    path(
        "comments/<int:pk>/update/", CommentUpdateApiView.as_view(), name="post-update"
    ),
    path(
        "comments/<int:pk>/delete/", CommentDeleteApiView.as_view(), name="post-delete"
    ),
]
