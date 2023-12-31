from django.forms import ModelForm
from .models import Post,Profile
from django import forms


class CreatePost(ModelForm):
    thumbnail = forms.ImageField()
    title = forms.TextInput()
    

    class Meta:
        model=Post
        exclude=['views','posted_on','post_id','author']

class CreateProfile(ModelForm):

    author_name = forms.TextInput()
    age = forms.NumberInput()
    occupation = forms.TextInput()
    deg = forms.TextInput()
    clg_yr = forms.TextInput()
    class Meta:
        model = Profile
        # fields = ['author_name','age','occupation','deg','clg_yr']
        exclude=['author_real','views']