from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)



class UsernameUpdate(forms.ModelForm):
    username=forms.CharField()
    class Meta:
        model=User
        fields=['username']


class EmailUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['email']

class PasswordUpdateForm(PasswordChangeForm):
    pass
