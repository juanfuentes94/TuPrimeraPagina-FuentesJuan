from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, SearchForm

def index(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()
    if form.is_valid() and form.cleaned_data['query']:
        posts = posts.filter(title__icontains=form.cleaned_data['query'])
    return render(request, 'index.html', {'posts': posts, 'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


# Create your views here.
