from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    bio = models.TextField(blank=True)
    name = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=60, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs ):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=60, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering =['-pk']

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def __str__(self):
        return f'{self.user.name} Post'



class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user= models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.user.name} Post'

    class Meta:
        ordering = ['-pk']

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'