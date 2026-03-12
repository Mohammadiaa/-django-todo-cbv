from django.urls import path,include
from . import views
from .views import ProfileView,EditProfileView
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("logout/", LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    #path("register/", views.register, name="register"),

    path("profile/",ProfileView.as_view(), name="user_profile"),
    path("profile/edit/",EditProfileView.as_view(), name="edit_profile")
]