from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.


def index(req):
    # return HttpResponse('Hello from post')

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latets Posts',
        'posts': posts
    }

    return render(req, 'post/index.html', context)


def details(req, id):
    post = Posts.objects.get(id)

    context = {
        'post': post
    }

    return render(req, 'post/details.html', context)
