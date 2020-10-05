
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = (
    path('', views.Kus,name="home"),
    path('about-me', views.about, name="about"),
    path('statii-moi', views.stats, name="statii"),
    path('create-stat', views.create, name = "create")
)
