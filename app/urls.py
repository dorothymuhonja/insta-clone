from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app import views as app_views

appname= 'app'

urlpatterns = [
    path('register/',app_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('profile/<str:username>/', app_views.profile, name='profile'),
    path('user_profile/<str:username>/', app_views.user_profile, name='user_profile'),
    path('post/<int:id>/', app_views.post_comment, name='comment'),
    path('search/', app_views.search_profile, name='search'),
    path('unfollow/<to_unfollow>/', app_views.unfollow, name='unfollow'),
    path('follow/<to_follow>/', app_views.follow, name='follow'),
    path('<post_id>/like', views.like, name='likePost'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)