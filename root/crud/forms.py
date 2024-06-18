from django.forms import ModelForm
from .models import BlogPost


class CreatePost(ModelForm):
    class Meta:
        model=BlogPost
        fields=['img','title','content','author']