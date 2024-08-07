from ..models import Aluno
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser

def get_students_by_class(req):
    if (req.method == 'GET'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            query = req.GET.get("turma")

            alunos = Aluno.objects.filter(turma__icontains=query)

            alunos_serialized = [aluno.to_dict() for aluno in alunos]

            return JsonResponse({'students': alunos_serialized})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
