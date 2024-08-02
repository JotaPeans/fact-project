from django.urls import path
from .views import signUp, User

app_name = 'autenticacao'
urlpatterns = [
    path('auth/user/create', view=signUp, name="create"),
    path('auth/user', view=User.as_view(), name="get"),
]