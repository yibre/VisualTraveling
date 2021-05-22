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

class SearchView(View):
    """This is the function for making the search view, not completed yet"""
    pass

class EditPostView(UpdateView):
    model = models.Post
    template_name = "posts/post_edit.html"
    fields = {
        "writter",
        "title",
        "location_info",
        "contents",
        "country",
        "latitude",
        "longitude",
    }

class EditPhotoView(UpdateView):

    model = models.Photo
    template_name = "posts/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        post_pk = self.kwargs.get("post_pk")
        return reverse("posts:photos", kwargs={"pk": post_pk})


class PostPhotosView(DetailView):
    model = models.Post
    template_name = "posts/post_photos.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        return post


class AddPhotoView(FormView):
    model = models.Photo
    template_name = "posts/photo_create.html"
    fields = ("caption", "file")
    form_class = forms.CreatePhotoForm
    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("posts:photos", kwargs={"pk": pk}))


class UploadPostView(FormView):
    """ for update the photos """

    form_class=forms.UploadPostForm
    template_name = "posts/post_create.html"

    def form_valid(self, form):
        post = form.save()
        post.save()
        messages.success(self.request, "Post Uploaded")
        return redirect(reverse("posts:detail", kwargs={"pk": post.pk}))

def delete_photo(request, post_pk, photo_pk):
    try:
        post = models.Post.objects.get(pk=post_pk)
        models.Photo.objects.filter(pk=photo_pk).delete()
        messages.success(request, "Photo Deleted")
        return redirect(reverse("posts:photos", kwargs={"pk": post_pk}))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))


def post_delete(request, pk):
    print("delete post function activated", pk)
    post = models.Post.objects.filter(pk=pk)
    post.delete()
    try:
        post = models.Post.objects.get(pk=pk)
        post.delete()
        print(f"should delete {pk}")
        print(post)
        message.success(request, "post deleted")
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))
