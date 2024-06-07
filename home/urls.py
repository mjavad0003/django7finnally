from django.urls import path
from .views import HomeView,PostDetailView,AboutUsView,edit_comment,delete_comment

urlpatterns  = [
    path('',HomeView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('aboutus/',AboutUsView.as_view(),name='aboutus'),
    path('edit/comment/<int:pk>/',edit_comment, name='edit_comment'),
    path('delete/comment/<int:pk>/',delete_comment, name='delete_comment'),
]