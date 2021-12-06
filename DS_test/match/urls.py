from django.urls import path
from match import views


urlpatterns = [ 
    path('match/', views.match, name="match"),
    path('match/M<int:match_id>/', views.match_detail, name='match_detail'),
    path('add/', views.add, name="add"),
    path('addmatch/', views.addmatch, name="addmatch"),
]