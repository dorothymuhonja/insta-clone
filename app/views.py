from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
from .models import Post, Comment, Profile, Follow, Likes
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from django.contrib import messages
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



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
    
    return render(request, 'registration/register.html', {'form': form })



@login_required
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
        'users': users,
    }

    return render(request, 'insta/index.html', params)


@login_required
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {
        'user_form': user_form,
        'profile_form': profile_form,
        'images':images,
    }
    return render(request, 'insta/profile.html', params)


@login_required
def user_profile(request, username):
    u_profile = get_object_or_404(User, username=username)
    if request.user == u_profile:
        return redirect('profile', username=request.user.username)
    user_posts = u_profile.profile.posts.all()

    followers = Follow.objects.filter(followed=u_profile.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False


    params = {
        'u_profile': u_profile,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    return render(request, 'insta/user_profile.html', params)


@login_required
def post_comment(request, id):
    image = get_object_or_404(Post, pk=id)
    # is_liked = False
    # if image.likes.filter(id=request.user.id).exists():
    #     is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    

    params = {
        'image': image,
        'form': form,
        # 'is_liked': is_liked,
        # 'total_likes': image.total_likes()
    }
    return render(request, 'insta/post_comment.html', params)

@login_required
def like(request,post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    
    liked = Likes.objects.filter(user=user, post=post).count()
    
    if not liked:
        like = Likes.objects.create(user=user,post=post)
        
        current_likes = current_likes + 1
        
    else:
        Likes.objects.filter(user=user,post=post).delete()

        current_likes = current_likes - 1
        
    post.likes = current_likes
    post.save() 
    
    return HttpResponseRedirect(reverse('index'))  


@login_required
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get('search_user')
        results = Profile.search_profile(name)
        print(results)
        message = f'name'

        params = {
            'results': results,
            'message': message
        }
        return render(request, 'insta/results.html', params)
    else:
        message = "You haven't searched for anyone"
    return render(request, 'insta/results.html', {'message': message})


def unfollow(request, to_unfollow):
    if request.method == 'GET':
        user_profile2 = Profile.objecets.get(pk=to_unfollow)
        unfollow_d = Follow.objects.filter(follower=request.user.profile, followed=user_profile2)
        unfollow_d.delete()
        return redirect('user_profile', user_profile2.user.username)

def follow(request, to_follow):
    if request.method == 'GET':
        user_profile3 = Profile.objects.get(pk=to_follow)
        follow_s = Follow(follower=request.user.profile, followed=user_profile3)
        follow_s.save()
        return redirect('user_profile', user_profile3.user.username)

