import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from .utils.get_fact_grade import getMediaAluno, transformNotasToObject
from autenticacao.models import CustomUser

import pandas as pd

from ..models import Aluno, Fact, Grupo
from .utils.create_fact import Fact as FactClass


@csrf_exempt
def import_fact(req):
    if (req.method == 'POST'):
        payload = get_jwt_token(req)

        try:
            file = req.FILES.get("file")
            name = req.POST.get("name")
            grupoId = req.POST.get("group")

            user = CustomUser.objects.get(pk=payload.get("id"))
            group = Grupo.objects.get(pk=int(grupoId))

            if (group.professor.id == user.id):
                df = pd.read_excel(file)

                try:
                    file = req.FILES["file"]
                    df = pd.read_excel(file)

                    notas = getMediaAluno(df)

                except Exception as e:
                    print(e)
                    return JsonResponse({"message": "Excel ou arquivo no formato inválido"}, status=400)

                alunos = []

                for nome_aluno, *_ in notas:
                    if (nome_aluno not in alunos):
                        alunos.append(nome_aluno)

                for nome_aluno in alunos:
                    aluno_data = list(
                        filter(lambda x: x[0] == nome_aluno, notas))

                    aluno_object = transformNotasToObject(aluno_data)

                    aluno = Aluno.objects.filter(nome=aluno_object["nome"])[0]

                    if (aluno):
                        fact = Fact.objects.create(
                            nome=name,
                            pensamento_critico_criatividade=aluno_object["pensamento_crítico_e_criatividade"],
                            comunicacao=aluno_object["comunicação"],
                            colaboracao=aluno_object["colaboração"],
                            qualidade_entregas=aluno_object["qualidade_das_entregas"],
                            presenca=aluno_object["presença"],
                            entrega_prazos=aluno_object["entregas_e_prazos"],
                            aluno=aluno,
                            grupo=group
                        )

                        fact.save()

                return JsonResponse({"message": "Fact importado com sucesso"})

            raise Exception('Esse grupo não lhe pertence')
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)

    return JsonResponse({}, status=405)
