from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser
from ..models import Grupo

@csrf_exempt
def add_teachers_to_group(req):
    if (req.method == "POST"):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            groupId = req.POST.get("groupId")
            teachersIds = req.POST.getlist('id')
            
            group = Grupo.objects.get(pk=int(groupId))
            group.sharedToProfessor.clear()

            for teacherId in teachersIds:
                teacher = CustomUser.objects.get(pk=int(teacherId))
                group.sharedToProfessor.add(teacher)

            group.save()

            return JsonResponse({"message": "Professores adicionados ao grupo com sucesso!"})

        except Exception as e:
            print(e)
            return JsonResponse({"message": "Nao autorizado"}, status=401)

    return JsonResponse({}, status=405)
