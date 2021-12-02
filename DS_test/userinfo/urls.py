from django.urls import path
from userinfo import views as user_views


urlpatterns = [ 
    path('login/', user_views.login, name="login"),
    path('register/', user_views.register, name="register"),
    path('logout/', user_views.logout, name="logout"),
    path('profile/', user_views.profile, name="profile"),
]