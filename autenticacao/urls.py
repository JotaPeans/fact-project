from django.urls import path
from . import views

app_name = 'autenticacao'
urlpatterns = [
    path('auth/user/create', views.SignUp.as_view(), name="root"),
    path('auth/user', views.User.as_view(), name="root"),
]