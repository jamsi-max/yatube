from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    tempate = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, tempate, context)


def group_posts(request, slug):
    tempate = 'posts/group_list.html'
    title = f'Записи сообщества {slug}.'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, tempate, context)
