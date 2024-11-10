from django.urls import path
from .views import SignUpView, GetUser, UploadProfilePictureView, UserMeView


urlpatterns = [
    path("create-account/", SignUpView.as_view(), name="sign_up"),
    path("user-detail/<int:pk>/", GetUser.as_view(), name="get-user"),
    path(
        "upload-profile-picture/",
        UploadProfilePictureView.as_view(),
        name="update-profile-picture",
    ),
    path("user-me/", UserMeView.as_view(), name="get-current-user"),
]
