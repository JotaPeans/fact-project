from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "feedbackApp"

urlpatterns = [
    path("", views.FeedBackView.as_view(), name="root"),
    path("group/<int:id>", views.GroupView.as_view(), name="group"),
    path("group/action/<int:id>", views.Group.as_view(), name="group_action"),
    path("group/deleting/<int:groupId>", views.deleteGroup.as_view(), name = "deleteGroup"),
    path("group/deletingAluno/<int:alunoId>", views.deleteGroup.as_view(), name = "deleteAluno"),
    path("logout/", views.logoutFunction, name="logout")
]