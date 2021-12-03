from django.urls import path
from attempts import views


urlpatterns = [ 
    path('attempts/', views.attempts, name="attempts"),
]