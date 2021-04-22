from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

class User(AbstractUser):

    """ custom user model """

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHINESE = "cn"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"), (LANGUAGE_CHINESE, "Chinese"))

    country = CountryField(null=True)
    avatar = models.ImageField(blank=True)
    bio = models.CharField(blank = True, max_length= 100)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)


"""
https://pypi.org/project/django-countries/ <- 설치함

"""