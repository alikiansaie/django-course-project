from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, Http404
from . models import Post
# Create your views here.


def index(request):
    return HttpResponse('index')


def post_list(request):
    posts = Post.published.all()
    context = {
        'posts': posts
    }

    return render(request, "blog/list.html", context)
    # {'posts': posts}) => if its gets more than one you should make a dic var

import datetime
def post_detail(request, id):
    post = get_object_or_404(Post , id=id , status = Post.Status.PUBLISHED)
    # try:
    #     post = Post.published.get(id=id)
    # except:
    #     raise Http404('Not Post Found !')
    context = {
        'post': post,
        'new_date':datetime.datetime.now()
    }
    return render(request, "blog/detail.html", context)

