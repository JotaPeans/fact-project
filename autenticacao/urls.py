from django.urls import path
from .views import signUp, getUser, get_csrftoken

app_name = 'autenticacao'
urlpatterns = [
    path('auth/get-csrftoken', view=get_csrftoken, name="get_token"),
    path('auth/user/create', view=signUp, name="create"),
    path('auth/user/<str:email>', view=getUser, name="get"),
]