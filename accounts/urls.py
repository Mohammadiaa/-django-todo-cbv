from django.urls import path
from . import views
from .views import ProfileView

app_name = "accounts"

urlpatterns = [
    path("profile/",ProfileView.as_view(), name="user_profile")
]