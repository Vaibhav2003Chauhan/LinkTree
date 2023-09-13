from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django.contrib.auth.models import User
from home.models import *


# update your profile 
class userForm(ModelForm):
    class Meta:
        model=userinformation
        fields='__all__'
        exclude=['user','mail']
        