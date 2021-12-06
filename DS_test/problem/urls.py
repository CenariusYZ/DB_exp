from django.urls import path
from problem import views


urlpatterns = [ 
    path('problem/', views.problem, name="problem"),
    path('problem/P<int:problem_id>/submit', views.submit, name="p_submit"),
    path('problem/P<int:problem_id>/', views.detail, name='detail'),
    path('problem/P<int:problem_id>/submit_code', views.submit_code, name="code_submit")
]