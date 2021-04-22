from django.contrib import admin
from django.db import models
from core import models as core_models

class Post(core_models.TimeStampedModel):
    writter = models.ForeignKey("users.User", related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    contents = models.TextField()
    likes = models.IntegerField()
    
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.caption



""" 
django google map: https://pypi.org/project/django-google-maps/ <- 이미설치해둠
https://django-map-widgets.readthedocs.io/en/latest/widgets/point_field_map_widgets.html
https://pypi.org/project/django-geoposition/ <- 설치 안 함
https://www.gyford.com/phil/writing/2017/03/16/django-admin-map/ <- 상당히 쓸만해보이는 장고 자료

구글 API 받았음
"""