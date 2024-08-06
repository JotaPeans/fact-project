import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

from ..models import Grupo
from .utils.create_fact import Fact as FactClass

@csrf_exempt
def create_fact(req):
    if (req.method == 'POST'):
        payload = get_jwt_token(req)

        data = json.loads(req.body)

        groupId = data.get("id")

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))
            grupo = Grupo.objects.get(pk=groupId)

            if(grupo.professor.id == user.id):
                alunos = list(grupo.alunos.all())

                alunos_nomes = [aluno.nome for aluno in alunos]
                alunos_emails = [aluno.email for aluno in alunos]

                fact = FactClass()

                fact = fact.create_fact(
                    email_address=user.email, alunos=alunos_nomes, emails=alunos_emails)

                if (fact["error"] == None):
                    return JsonResponse({"url": fact["formUrl"]})
            
            raise Exception('Esse grupo não lhe pertence')
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)

    return JsonResponse({}, status=405)
