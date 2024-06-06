from django.urls import path
from .views import HomeView,PostDetailView,AboutUsView

urlpatterns  = [
    path('',HomeView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('aboutus/',AboutUsView.as_view(),name='aboutus'),
]