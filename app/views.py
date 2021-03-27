from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
from .models import Post, Comment, Profile, Follow
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users
    }

    return render(request, 'insta/index.html')