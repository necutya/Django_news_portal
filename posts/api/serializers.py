from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)

from posts.models import Post, Comment


class PostSerializer(ModelSerializer):
    """ Serializer for Post model """

    author = SerializerMethodField()
    num_votes = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="posts-api:post")

    class Meta:
        model = Post
        fields = ["id", "url", "title", "link", "creation_date", "author", "num_votes"]

    def get_author(self, obj):
        return str(obj.author)

    def get_num_votes(self, obj):
        return obj.num_votes


class PostDetailSerializer(ModelSerializer):
    """ Serializer for detailed view """

    author = SerializerMethodField()
    comments = SerializerMethodField()
    num_votes = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "author",
            "num_votes",
            "comments",
        ]

    def get_author(self, obj):
        return str(obj.author)

    def get_comments(self, obj):
        comments = CommentSerializer(
            Post.objects.get(pk=obj.id).comment_set.all(), many=True
        ).data
        return comments

    def get_num_votes(self, obj):
        return obj.num_votes


class PostCreateSerializer(ModelSerializer):
    """ Serializer fo creating a post """

    class Meta:
        model = Post
        fields = [
            "title",
            "link",
        ]


class CommentListSerializer(ModelSerializer):
    """ Serializers for lists og Comments"""

    related_to = SerializerMethodField()
    author = SerializerMethodField()
    url = HyperlinkedIdentityField(view_name="posts-api:comment")

    class Meta:
        model = Comment
        fields = [
            "id",
            "url",
            "content",
            "date_published",
            "author",
            "related_to",
        ]

    def get_related_to(self, obj):
        return obj.post.title

    def get_author(self, obj):
        return obj.author.username


class CommentSerializer(ModelSerializer):
    """ One comment Serializer """

    related_to = SerializerMethodField()
    author = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "date_published",
            "author",
            "related_to",
        ]

    def get_related_to(self, obj):
        return obj.post.title

    def get_author(self, obj):
        return obj.author.username


class CommentCreateSerializer(ModelSerializer):
    """ Comment creation Serializer"""

    class Meta:
        model = Comment
        fields = [
            "content",
            "post",
        ]
