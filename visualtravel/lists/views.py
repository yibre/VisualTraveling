from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . import models
# Create your views here.

class PostsListView(ListView):
    """blablabla"""
    model = models.List
    template_name = "lists/posts_list.html"