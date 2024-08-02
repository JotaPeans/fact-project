from ..models import Aluno
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

def get_students(req):
    if (req.method == 'GET'):
        alunos = Aluno.objects.all()
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            alunos_serialized = [aluno.to_dict() for aluno in alunos]

            return JsonResponse({'students': alunos_serialized})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
