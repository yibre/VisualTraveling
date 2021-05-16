from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.contrib import messages


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
        "country",
        "location_info",
        "latitude",
        "longitude"
    }

class EditPhotoView(UpdateView):

    model = models.Photo
    template_name = "posts/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        room_pk = self.kwargs.get("post_pk")
        return reverse("posts:photos", kwargs={"pk": post_pk})


class UploadPostView(FormView):
    """ for update the photos """

    form_class=forms.UploadPostForm
    template_name = "posts/post_upload.html"

    def form_valid(self, form):
        post = form.save()
        post.save()
        messages.success(self.request, "Post Uploaded")
        return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))