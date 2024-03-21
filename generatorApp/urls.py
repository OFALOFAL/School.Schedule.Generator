from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "generatorApp"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.LogoutUserView, name='logout'),


    path('upload/<int:schedule_id>', views.upload, name='upload'),
    path('upload/<str:file_name>/<int:schedule_id>', views.get_upload_file, name='get-upload-file'),
    path('settings/<int:schedule_id>', views.schedule_settings, name='settings'),
    path('create_schedule', views.create_schedule, name='create-schedule'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
