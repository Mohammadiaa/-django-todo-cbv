from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProfileView(TemplateView):
    template_name = "profile/profile.html"

class EditProfileView(TemplateView):
    template_name = "profile/profile_form.html"