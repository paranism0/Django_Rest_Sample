from django.urls import path
from .views import RegisterApiView , UserDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
        path('register/', RegisterApiView.as_view(), name='register'),
        path("login/",obtain_auth_token , name="login"),
        path('profile/',UserDetailView.as_view() , name = "profile")
]
