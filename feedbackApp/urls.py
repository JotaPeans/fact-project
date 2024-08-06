from django.urls import path

from .group.get_group_by_id import get_group_by_id
from .group.delete_group import delete_group
from .group.get_groups import get_groups
from .group.create_group import create_group

from .student.get_student_fact import get_student_fact
from .student.get_students import get_students
from .student.create_student import create_student
from .student.update_student import update_student

from .fact.import_fact import import_fact
from .fact.create_fact import create_fact

app_name = "feedbackApp"

urlpatterns = [
    path("groups", get_groups, name="get_groups"),
    path("groups/<int:id>", get_group_by_id, name="get_group_by_id"),
    path("groups/delete/<int:id>", delete_group, name="delete_group"),
    path("groups/create", create_group, name="create_group"),

    path("students", get_students, name="get_students"),
    path("students/<int:id>/fact", get_student_fact, name="get_student_fact"),
    path("students/create", create_student, name="create_student"),
    path("students/update", update_student, name="update_student"),

    path("fact/import", import_fact, name="import_fact"),
    path("fact/create", create_fact, name="create_fact"),

    # path("", views.FeedBackView.as_view(), name="root"),
    # path("addAdminToGroup", views.addAdmin, name = "add_admin"),
    # path("changeInfo", views.changeAlunoInfo, name = "change_info"), 

    # path("group/<int:id>", views.GroupView.as_view(), name="group"),
    # path("group/deleting/<int:groupId>", views.deleteGroup.as_view(), name = "deleteGroup"),
    # path("group/<int:id>/edit/", views.GroupStudent.as_view(), name="edit"),
    # path("group/<int:id>/alunos/", views.getAlunos, name="getAlunos"),

    # path("aluno/edit", views.AlunoEdit.as_view(), name="editAluno"),

    # path("fact/create/<int:groupId>", views.FactCreate.as_view(), name="createFact"),
]