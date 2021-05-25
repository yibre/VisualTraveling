from django.contrib import admin
from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from django.urls import reverse

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.caption


class Post(core_models.TimeStampedModel):
    writter = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    contents = models.TextField()
    likes = models.IntegerField( default = 0)
    location_info = models.CharField(max_length=80, blank=True, null=True)
    country = CountryField(blank=True, null=True, blank_label='South Korea')
    camera = models.CharField(max_length=80, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    love = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

    def get_photos(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None




""" 
django google map: https://pypi.org/project/django-google-maps/ <- 이미설치해둠
https://django-map-widgets.readthedocs.io/en/latest/widgets/point_field_map_widgets.html
https://pypi.org/project/django-geoposition/ <- 설치 안 함
https://www.gyford.com/phil/writing/2017/03/16/django-admin-map/ <- 상당히 쓸만해보이는 장고 자료

구글 API 받았음
"""