from django.urls import path
from . import views


app_name = "lists"

urlpatterns = [
    path("mylist/", views.PostsListView.as_view(), name="postlists"),
]