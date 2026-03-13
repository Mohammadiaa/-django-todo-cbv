from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileEditForm
# Create your views here.

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = "profile/profile.html"

class EditProfileView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "profile/profile_form.html"
    success_url = "/accounts/profile/"


    def get_object(self, queryset=None):
        return self.request.user.profile
    