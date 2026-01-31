from django import forms
from .models import User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_image', 'location', 'sustainability_interests']