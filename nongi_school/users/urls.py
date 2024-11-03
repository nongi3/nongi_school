from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('save_profile/', views.edit_profile, name='save_profile'),
]
