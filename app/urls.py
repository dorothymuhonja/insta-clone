from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app import views as app_views


urlpatterns = [
    path('register/',app_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)