from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "feedbackApp"

urlpatterns = [
    path("", views.FeedBackView.as_view(), name="root"),
    path("group/<int:id>", views.GroupView.as_view(), name="group"),
    path("logout/", views.logoutFunction, name="logout")
]