from django.urls import path
from posts import views as post_views

app_name = "core"

urlpatterns = [path("", post_views.all_posts, name="home")]