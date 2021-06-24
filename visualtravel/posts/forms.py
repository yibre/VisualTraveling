from django import forms
from django_countries.fields import CountryField
from . import models

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        post = models.Post.objects.get(pk=pk)
        photo.post = post
        photo.save()

class UploadPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "title",
            "contents",
            "country",
            "location_info",
            "camera",
            "latitude",
            "longitude",
            "file",
        )

    def save(self, *args, **kwargs):
        post = super().save(commit=False)
        return post

class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        post = models.Post.objects.get(pk=pk)
        photo.post = post
        photo.save()