from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditPostView.as_view(), name="edit"),
    path("upload/", views.UploadPostView.as_view(), name="upload"),
    path("<int:pk>/delete/", views.post_delete, name="delete"),
    path("search/", views.search, name="search"),
    path("<int:pk>/photos/", views.PostPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
    path("favorite/", views.FavoritePlacesView.as_view(), name="favlist"),
    path("<int:pk>/addfav/", views.add_favlist, name="add-fav"),
    path("<int:pk>/deletefav/", views.delete_favlist, name="delete-fav"),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path(
        "<int:post_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
]