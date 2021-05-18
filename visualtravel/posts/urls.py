from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditPostView.as_view(), name="edit"),
    path("upload/", views.UploadPostView.as_view(), name="upload"),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
]
"""
    path(
        "<int:post_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
"""