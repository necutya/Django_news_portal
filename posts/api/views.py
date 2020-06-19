from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import IsAuthenticated, AllowAny

from posts.models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    CommentListSerializer,
    CommentSerializer,
    CommentCreateSerializer,
)


class PosListApiView(ListAPIView):
    """ API view for posts list """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostDetailApiView(RetrieveAPIView):
    """ API view for detailed posts """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]


class PostCreateApiView(CreateAPIView):
    """ API view for posts list """

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateApiView(RetrieveUpdateAPIView):
    """ API view for post updating """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PostVoteApiView(APIView):
    """ API view for post voting """

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        Post.objects.get(pk=pk).votes.add(request.user)
        post = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostDeleteApiView(DestroyAPIView):
    """ API view for post deleting """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListApiView(ListAPIView):
    """ API view for comments list """

    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


class CommentDetailApiView(RetrieveAPIView):
    """ API view for detailed comment """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


class CommentCreateApiView(CreateAPIView):
    """ API view for comment creation """

    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentUpdateApiView(RetrieveUpdateAPIView):
    """ API view for comment updating """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentDeleteApiView(DestroyAPIView):
    """ API view for comment deleting """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
