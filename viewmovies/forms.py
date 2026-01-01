from django import forms 
from .models import Ratings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ["rating"]
        

""" for creating new users """        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]