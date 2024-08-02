from ..models import Grupo
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

def get_group_by_id(req, id):
    if (req.method == 'GET'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            group = Grupo.objects.get(pk=id)

            if(user.id == group.professor.id):
                return JsonResponse({'group': group.to_dict()})
            else:
                raise Exception('Esse grupo não lhe pertence')
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
