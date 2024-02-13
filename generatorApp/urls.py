from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "generatorApp"
urlpatterns = [
    path('login-register/', views.login_register, name='login_register'),
    path('login-register/login/', views.login_page, name='login'),
    path('login-register/register/', views.register_page, name='register'),
    path('home/', views.home, name='home'),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)