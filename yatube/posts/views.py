from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post, Group


def index(request):
    tempate = 'posts/index.html'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
    }
    return render(request, tempate, context)


def group_posts(request, slug):
    tempate = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'posts': posts,
    }
    return render(request, tempate, context)
