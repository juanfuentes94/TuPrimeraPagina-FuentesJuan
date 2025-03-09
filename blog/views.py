from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm
from .mixins import SuccessMessageMixin


@login_required
def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        qs = super().get_queryset()
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['posts']:
            context['no_results'] = "No posts found."
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
    success_message = "Post created successfully!"


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')
    success_message = "Post updated successfully!"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
