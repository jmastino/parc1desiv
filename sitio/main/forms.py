from django import forms
from .models import Blog

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

      

class BlogForm(forms.ModelForm):
    author = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={
        'placeholder': '*author name..',
        }))
    name = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={
        'placeholder':'*Full name ..',
        }))
    description = forms.CharField(max_length=500,required=True,widget=forms.TextInput(attrs={
        'placeholder':'*description..',
    }))
    body = forms.CharField(max_length=1000,required=True,widget=forms.Textarea(attrs={
        'placeholder':'*body info .. ',
    }))
    image = forms.ImageField()

    class Meta:
        model = Blog
        fields = ['author','name','description','body','image']