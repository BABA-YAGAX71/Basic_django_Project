from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo', 'content']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")    



