from django.urls import path,include
from . import views
from .views import ProfileView,EditProfileView,registerView
from django.contrib.auth.views import LogoutView,LoginView
from .forms import EmailAuthenticationForm

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),

    path("login/", LoginView.as_view(template_name="registration/login.html",authentication_form=EmailAuthenticationForm), name="login"),
 
    path("logout/", LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    path("register/",registerView.as_view(), name="register"),

    path("profile/",ProfileView.as_view(), name="user_profile"),
    path("profile/edit/",EditProfileView.as_view(), name="edit_profile")
]