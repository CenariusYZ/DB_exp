from django.urls import path
from match import views


urlpatterns = [ 
    path('match/', views.match, name="match"),
]