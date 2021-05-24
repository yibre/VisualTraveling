from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . import models
# Create your views here.

class PostsListView(ListView):
    """blablabla"""
    model = models.List
    template_name = "lists/list.html"
    # context = model.objects.all()[:1].get()
    context_object_name = 'posts'

##request.user.users.all()
    def get_object(self, queryset=None):
        onelist = super().get_object(queryset=queryset)
        posts = onelist.posts.all()
        return posts