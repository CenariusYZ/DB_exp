from django.urls import path
from problem import views


urlpatterns = [ 
    path('problem/', views.problem, name="problem"),
    path('problem/pp<int:problem_id>/', views.detail, name='detail'),
]