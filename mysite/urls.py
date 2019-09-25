from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:pk>/', views.delete_image, name='delete_image'),
    path('upload/', views.upload_image, name='upload_image'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
