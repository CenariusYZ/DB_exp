from django.urls import path
from soj import views


urlpatterns = [ 
    path('', views.index, name="index"),
]