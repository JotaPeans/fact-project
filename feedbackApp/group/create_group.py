import json
from ..models import Grupo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

@csrf_exempt
def create_group(req):
    if (req.method == 'POST'):
        payload = get_jwt_token(req)

        data = json.loads(req.body)

        groupName = data.get("name")

        if(len(groupName) < 5):
            return JsonResponse({'message': "O nome do grupo precisa ter no mínimo 5 caracteres!"}, status=400)
        
        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            group = Grupo.objects.create(nome=groupName, professor=user)
            group.save()

            return JsonResponse({'message': 'Grupo criado com sucesso!', 'group': group.to_dict()})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
