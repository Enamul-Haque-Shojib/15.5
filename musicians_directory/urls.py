
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_musicians_directory, name='show_musicians_directory'),
    path('author/', include('author.urls')),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
]
