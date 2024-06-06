from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "feedbackApp"

urlpatterns = [
    path("", views.FeedBackView.as_view(), name="root"),
    path("group/<int:id>", views.GroupView.as_view(), name="group"),
    path("group/deleting/<int:groupId>", views.deleteGroup.as_view(), name = "deleteGroup"),
    path("group/deletingAluno/<int:alunoId>", views.deleteGroup.as_view(), name = "deleteAluno"),
    path("logout/", views.logoutFunction, name="logout"),
    path("group/<int:id>/delete_alunos/", views.delete_alunos, name="delete_alunos"),
    path("group/<int:id>/add_alunos/", views.add_alunos, name="delete_alunos")
]