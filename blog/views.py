from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostListViewAll(ListView):
    model = Post


class PostCreateView(CreateView):
    fields = ("title", "text", "image", "is_published")
    success_url = reverse_lazy("blog:post_list")
    model = Post

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", args=[self.object.pk])


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "text", "image", "is_published")
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")


class PublishPost(UpdateView):
    model = Post
    fields = []
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        self.object.is_published = True
        self.object.save()
        return super().form_valid(form)
