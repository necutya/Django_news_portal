from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    """ Post Model"""

    title = models.CharField(max_length=60)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    votes = models.ManyToManyField(User, related_name="user_votes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def num_votes(self):
        """ Return count of votes """
        return self.votes.count()

    @classmethod
    def delete_votes(cls):
        """ Delete all votes """
        for post in Post.objects.all():
            post.votes.clear()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ Comment Model """

    content = models.TextField(max_length=150)
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
