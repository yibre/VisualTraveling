from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditPostView.as_view(), name="edit"),   
]