from django.urls import path
from problem import views


urlpatterns = [ 
    path('problem/', views.problem, name="problem"),
    path('problem/P<int:problem_id>/', views.detail, name='detail'),
]