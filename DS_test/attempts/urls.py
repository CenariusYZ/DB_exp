from django.urls import path
from attempts import views


urlpatterns = [ 
    path('attempts/', views.attempts, name="attempts"),
    path('attempts/?s=<searchword>/page=<page_index>/', views.attempts_page, name="attempts_page"),
]