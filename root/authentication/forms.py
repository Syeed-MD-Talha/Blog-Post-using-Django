from django import forms  
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)



class PasswordUpdateForm(PasswordChangeForm):
    pass



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=User 
        fields=['username','first_name','last_name','email']
