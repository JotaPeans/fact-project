from ..models import Grupo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from autenticacao.models import CustomUser

@csrf_exempt
def delete_group(req, id):
    if (req.method == 'DELETE'):
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            group = Grupo.objects.get(pk=id)
            if(user.id == group.professor.id):
                group.delete()

                return JsonResponse({'message': 'Grupo deletado com sucesso'})
            else:
                raise Exception('Esse grupo não lhe pertence')
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
