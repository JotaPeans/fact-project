from ..models import Aluno
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser
from ..models import Fact

def get_student_fact(req, id):
    if (req.method == 'GET'):
        payload = get_jwt_token(req)

        try:
            facts = Fact.objects.filter(aluno__id=id)

            user = CustomUser.objects.get(pk=payload.get("id"))

            facts_serialized = [fact.to_dict() for fact in facts]

            return JsonResponse({'facts': facts_serialized})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
