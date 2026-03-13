# accounts/forms.py
from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "avatar", "bio"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }
