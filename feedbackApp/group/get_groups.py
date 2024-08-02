from ..models import Grupo
from django.http import JsonResponse
from autenticacao.utils.get_jwt_token import get_jwt_token
from feedbackApp.models import CustomUser

def get_groups(req):
    if (req.method == 'GET'):
        allowed_groups = []
        groups = Grupo.objects.all()
        payload = get_jwt_token(req)

        try:
            user = CustomUser.objects.get(pk=payload.get("id"))

            for group in groups:
                professors = list(group.sharedToProfessor.all())

                if (group.professor.email == user.email):
                    allowed_groups.append(group.to_dict())

                else:
                    for professor in professors:
                        if (user == professor):
                            allowed_groups.append(group.to_dict())

            return JsonResponse({'groups': allowed_groups})
        
        except Exception as e:
            print(e)
            return JsonResponse({'message': "Nao autorizado"}, status=401)
    
    return JsonResponse({}, status=405)
