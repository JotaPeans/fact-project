from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "feedbackApp"

urlpatterns = [
    path("", views.FeedBackView.as_view(), name="root"),
    path("addAdminToGroup", views.addAdmin, name = "add_admin"),
    path("changeInfo", views.changeAlunoInfo, name = "change_info"), 

    path("group/<int:id>", views.GroupView.as_view(), name="group"),
    path("group/deleting/<int:groupId>", views.deleteGroup.as_view(), name = "deleteGroup"),
    path("group/<int:id>/edit/", views.GroupStudent.as_view(), name="edit"),
    path("group/<int:id>/alunos/", views.getAlunos, name="getAlunos"),

    path("aluno/edit", views.AlunoEdit.as_view(), name="editAluno"),

    path("fact/create/<int:groupId>", views.FactCreate.as_view(), name="createFact"),

    path("populate", views.populate, name="populate"),
    path("logout/", views.logoutFunction, name="logout"),
]