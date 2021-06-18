from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
   

class HomeView(ListView):
    """ home view definition """

    model = models.Post
    context_object_name = "posts"


class PostDetail(DetailView):
    """ Post Detail View Definition """

    model = models.Post


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        #print(query)
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(contents__icontains=query) | Q(location_info__icontains=query) | Q(country__icontains=query) |Q(camera__icontains=query)
            results= models.Post.objects.filter(lookups).distinct()
            #print("result is ", results)
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, "posts/search.html", context)
        else:
            return render(request, "posts/search.html")
    else:
        return render(request, "posts/search.html")

# http://www.learningaboutelectronics.com/Articles/How-to-add-search-functionality-to-a-website-in-Django.php
# how to make a search function in here

class EditPostView(UpdateView):
    model = models.Post
    template_name = "posts/post_edit.html"
    fields = {
        "title",
        "location_info",
        "contents",
        "country",
        "latitude",
        "longitude",
        "file"
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
    try:
        post = models.Post.objects.get(pk=pk)
        post.delete()
        messages.success(request, "post deleted")
        return redirect(reverse("core:home"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))


class FavoritePlacesView(ListView):
    """ This is for making favorite list """

    template_name="posts/fav_list.html"
    context_object_name = "favposts"
    queryset = models.Post.objects.filter(love=True)


def add_favlist(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = True
        post.save()
        # return HttpResponseRedirect(request.path_info)
        return redirect(reverse("posts:detail", kwargs={"pk": pk}))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))


def delete_favlist(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = False
        post.save()
        return redirect(reverse("posts:detail", kwargs={"pk": pk}))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))

def add_favlist_main(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = True
        post.save()
        return redirect(reverse("core:home"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))


def delete_favlist_main(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = False
        post.save()
        return redirect(reverse("core:home"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))

def add_favlist_search(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = True
        post.save()
        return redirect(reverse("posts:search"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))

def delete_favlist_search(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = False
        post.save()
        return redirect(reverse("posts:search"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))

def delete_favlist_fav(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.love = False
        post.save()
        return redirect(reverse("posts:favlist"))
    except models.Post.DoesNotExist:
        return redirect(reverse("core:home"))