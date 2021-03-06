from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='A valid email address is required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=250, help_text='A valid email address is required')
    

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'caption')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']