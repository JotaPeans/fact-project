from django.urls import path
from .views import signUp, getUser, get_csrftoken, auth

app_name = 'autenticacao'
urlpatterns = [
    path('', view=auth, name="jwt"),
    path('get-csrftoken', view=get_csrftoken, name="get_token"),
    path('user/create', view=signUp, name="create"),
    path('user/<str:email>', view=getUser, name="get"),
]