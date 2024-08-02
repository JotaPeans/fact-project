import pandas as pd

from ..models import Aluno
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

from ..get_students_excel import createStudentsUsingExcelFile

@csrf_exempt
def create_student(req):
    if (req.method == 'POST'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))
            try:
                file = req.FILES.get('file')
                
                if(file):
                    df = pd.read_excel(file)
                    createStudentsUsingExcelFile(df)
                    return JsonResponse({'message': "Alunos criado com sucesso!"})
                else:
                    matricula = req.POST.get("matricula")
                    nome = req.POST.get("nome")
                    email_school = req.POST.get("email-school")
                    turma = req.POST.get("turma")

                    aluno = Aluno.objects.filter(email=email_school)

                    if(len(aluno) >= 1):
                        return JsonResponse({'message': "Aluno já cadastrado"}, status=400)
                    
                    Aluno.objects.create(matricula=matricula, nome=nome, email=email_school, turma=turma)
                    return JsonResponse({'message': "Aluno criado com sucesso!"})
                
            except Exception as e:
                print("exeption at 'addStudent' method - ", e)
                return JsonResponse({'message': "Erro ao criar alunos a partir do arquivo"}, status=400)
            
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)

    
    return JsonResponse({}, status=405)
