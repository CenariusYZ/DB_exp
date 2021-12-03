from django.urls import path
from problem import views


urlpatterns = [ 
    path('problem/', views.problem, name="problem"),
]