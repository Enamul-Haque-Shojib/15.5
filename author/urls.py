
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
   
]
