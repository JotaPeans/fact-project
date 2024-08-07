from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser
from ..models import Fact

def get_group_facts(req, id):
    if (req.method == 'GET'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            facts = Fact.objects.filter(grupo__id=id)
            
            facts_serialized = [fact.to_dict() for fact in facts]

            return JsonResponse({'facts': facts_serialized})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
