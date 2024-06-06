from django.urls import path
from .views import SignUpView,LoginView,LogoutView,ProfileView

urlpatterns = [
    path('signup/',SignUpView , name='signup'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
    path('profile/',ProfileView,name='profile'),
]