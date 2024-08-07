from django.urls import path

from .group.get_group_by_id import get_group_by_id
from .group.get_group_facts import get_group_facts
from .group.delete_group import delete_group
from .group.get_groups import get_groups
from .group.create_group import create_group

from .student.get_student_fact import get_student_fact
from .student.get_students import get_students
from .student.create_student import create_student
from .student.update_student import update_student

from .teacher.get_teachers import get_teachers
from .teacher.add_teachers_to_group import add_teachers_to_group
from .teacher.get_teachers_by_group import get_teachers_by_group

from .fact.import_fact import import_fact
from .fact.create_fact import create_fact

app_name = "feedbackApp"

urlpatterns = [
    path("groups", get_groups, name="get_groups"),
    path("groups/<int:id>", get_group_by_id, name="get_group_by_id"),
    path("groups/<int:id>/fact", get_group_facts, name="get_group_facts"),
    path("groups/delete/<int:id>", delete_group, name="delete_group"),
    path("groups/create", create_group, name="create_group"),

    path("students", get_students, name="get_students"),
    path("students/<int:id>/fact", get_student_fact, name="get_student_fact"),
    path("students/create", create_student, name="create_student"),
    path("students/update", update_student, name="update_student"),

    path("teachers", get_teachers, name="get_teachers"),
    path("teachers/group/<int:id>", get_teachers_by_group, name="get_teachers_by_group"),
    path("teachers/group/add", add_teachers_to_group, name="add_teachers_to_group"),

    path("fact/import", import_fact, name="import_fact"),
    path("fact/create", create_fact, name="create_fact"),
]