from django.contrib import admin
from .models import Profile, Post, Comment, Follow,Likes

admin.site.site_header = 'Insta-Clone Admin'
admin.site.site_title = 'Insta-Clone Admin Area'
admin.site.index_title = 'Welcome to Insta-Clone admin area'

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Likes)


