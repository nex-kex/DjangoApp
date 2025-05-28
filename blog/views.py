from django.shortcuts import render
from .models import Post
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)


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


class PostCreateView(CreateView):
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy("blog:post_list")
    model = Post

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
        return reverse("blog:post_list", args=[self.kwargs.get("pk")])


class PostDeleteView(DetailView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
