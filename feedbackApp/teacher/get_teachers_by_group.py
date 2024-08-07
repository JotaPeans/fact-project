from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser
from ..models import Grupo

def get_teachers_by_group(req, id):
    if (req.method == 'GET'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))
            
            grupo = Grupo.objects.get(pk=id)
            teachers = grupo.sharedToProfessor.all()
            
            teachers_serialized = [teacher.to_dict() for teacher in teachers]

            return JsonResponse({'teachers': teachers_serialized})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
