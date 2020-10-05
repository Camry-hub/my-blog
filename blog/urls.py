from django.urls import path
from . import views
urlpatterns = [
    path('kuki', views.post_list, name='post_list'),
]