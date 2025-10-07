from django.urls import path
from . import views

urlpatterns = [
    # Define your app-specific URL patterns here
    
    path('', views.hello_world),
    path('about/', views.about),
]