import json
from ..models import Grupo, Aluno
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser


@csrf_exempt
def update_group_students(req):
    if (req.method == "POST"):
        payload = get_jwt_token(req)

        groupId = req.POST.get("groupId")
        studentIds = req.POST.getlist("id")

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            group = Grupo.objects.get(id=int(groupId))
            
            group.alunos.clear()
            for studentId in studentIds:
                aluno = Aluno.objects.get(pk=studentId)
                group.alunos.add(aluno)

            group.save()

            return JsonResponse({"message": "Grupo atualizado com sucesso!"})

        except Exception as e:
            print(e)
            return JsonResponse({"message": "Nao autorizado"}, status=401)

    return JsonResponse({}, status=405)
