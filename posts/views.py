from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.contrib import messages

from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    """ Class-based generic view for posts lists """

    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        """ Sort by numbers of votes list """
        return sorted(Post.objects.all(), key=lambda x: -x.num_votes)


class UserPostListView(ListView):
    """ Class-based generic view for users posts lists """

    model = Post
    template_name = "posts/user_posts.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        """ Sort by numbers of votes list """
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return sorted(
            Post.objects.filter(author=user).all(), key=lambda x: -x.num_votes
        )


class PostDetailedView(DetailView):
    """ Class-based generic view for detailed post """

    model = Post
    template_name = "posts/post.html"

    def get_context_data(self, **kwargs):
        """ Add form adn comments to context data """
        context = super().get_context_data(**kwargs)
        context["comments"] = self.get_object().comment_set.all()
        context["form"] = CommentForm()
        return context


class CommentFormView(FormView):
    """ Class-based form view """

    form_class = CommentForm

    def get_success_url(self):
        """ Create a comments if form is valid """
        Comment.objects.create(
            content=self.request.POST["content"],
            author=self.request.user,
            post_id=self.request.POST["post_id"],
        )
        messages.success(self.request, "A comment has been successfully created")
        return reverse("posts:post", kwargs={"pk": self.request.POST["post_id"]})


class PostCreateView(LoginRequiredMixin, CreateView):
    """ Class-based view for post creation """

    model = Post
    fields = ["title", "link"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "A post has been successfully created")
        return reverse("posts:home")


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class-based generic view for post updating """

    model = Post
    fields = ["title", "link"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Check if user, who request an action, is author"""
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        messages.success(self.request, "A post has been successfully updated")
        return reverse("posts:home")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Class-based generic view for post deleting """

    model = Post

    def test_func(self):
        """ Check if user, who request an action, is author"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, "A post has been successfully deleted")
        return reverse("posts:home")


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class-based view for comment updating """

    model = Comment
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.get_object().post
        return super().form_valid(form)

    def test_func(self):
        """ Check if user, who request an action, is author"""
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        messages.success(self.request, "A comment has been successfully updated")
        return reverse("posts:post", kwargs={"pk": self.get_object().post_id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Class-based view for comment deleting """

    model = Comment

    def test_func(self):
        """ Check if user, who request an action, is author"""
        comment = self.get_object()
        self.post_id = comment.post_id
        if self.request.user == comment.author:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, "A post has been successfully deleted")
        return reverse("posts:post", kwargs={"pk": self.post_id})


@login_required
def vote(request, pk):
    """ Vote for post """
    Post.objects.get(pk=pk).votes.add(request.user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


def about(request):
    """ About page """
    return render(request, "posts/about.html", {"title": "About"})
