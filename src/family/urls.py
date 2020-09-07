from django.contrib import admin
from django.urls import path, include
from .views import daughter, myself, wife, home, welcome, contact


urlpatterns = [
    
    path('', welcome, name='family_welcome'),
    path('home/', home, name='family_home'),
    path('wife/', wife, name='family_wife'),
    path('myself/', myself, name='family_about_myself'),
    path('daughter/', daughter, name='family_daughter'),
    path('contact/', contact, name='family_contact')   
]

