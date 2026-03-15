from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileEditForm
from .models import User
from .forms import RegisterForm
from django.views import View
from django.contrib.auth.views import LoginView as AuthLoginView
from .forms import EmailAuthenticationForm
from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile/profile.html"


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = "profile/profile_form.html"
    success_url = "/accounts/profile/"

    def get_object(self, queryset=None):
        return self.request.user.profile

@method_decorator(ensure_csrf_cookie, name="dispatch")
class registerView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = "/accounts/login/"

 



class LoginView(AuthLoginView):
    template_name = "registration/login.html"
    authentication_form = EmailAuthenticationForm
    
