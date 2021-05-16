from django.views.generic import ListView, DetailView, View, UpdateView
from django.shortcuts import render
from . import models


class HomeView(ListView):
    """ home view definition """

    model = models.Post
    context_object_name = "posts"


class PostDetail(DetailView):
    """ Post Detail View Definition """

    model = models.Post

class EditPostView(UpdateView):
    model = models.Post
    template_name = "posts/post_edit.html"
    fields = {
        "title",
        "writter",
        "contents",
        "latitude",
        "longitude"
    }

"""
def post_detail(request, pk):
    print(pk)
    return render(request, "posts/detail.html")

def all_posts(request):
    all_posts = models.Post.objects.all()
    return render(request, "posts/post.html", context={"postinfo": all_posts})
"""