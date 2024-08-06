from ..models import Aluno
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from django.views.decorators.csrf import csrf_exempt
from feedbackApp.models import CustomUser

@csrf_exempt
def update_student(req):
    if (req.method == "POST"):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            alunoId = req.POST.get("id")
            nome = req.POST.get("nome")
            email = req.POST.get("email")
            matricula = req.POST.get("matricula")
            turma = req.POST.get("turma")

            try:
                aluno = Aluno.objects.get(pk=alunoId)

                aluno.nome = nome
                aluno.email = email
                aluno.matricula = matricula
                aluno.turma = turma

                aluno.save()

                return JsonResponse({"message": "Aluno atualizado com sucesso!"})

            except Exception as e:
                print(e)
                return JsonResponse({"message": "Erro ao atualizar o aluno"}, status=400)

        except Exception as e:
            print(e)
            return JsonResponse({"message": "Nao autorizado"}, status=401)

    return JsonResponse({}, status=405)
