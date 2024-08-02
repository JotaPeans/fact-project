from django.http.response import JsonResponse
from django.views import View
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import json


class User(View):
    def get(self, req):
        print(req)
        return JsonResponse({"id": "asd1kj23hjdjk12h3k12j"})


@csrf_exempt
def signUp(req):
    if req.method == 'POST':
        csrf_token = get_token(req)
        data = json.loads(req.body)

        id = data.get("id")
        name = data.get("name")
        email = str(data.get("email"))
        image = data.get("image")

        if (email.endswith("@cesar.school")):
            user = CustomUser.objects.filter(email=email)
            print(user)

            if (len(user) >= 1):
                return JsonResponse({"message": "Usuário já existe", "csrftoken": csrf_token}, status=400)

            CustomUser.objects.create(
                email=email, image=image, username=name, first_name=name, providerId=id, role="aluno")

            response = JsonResponse(
                {"message": "Usuário criado com sucesso", "csrftoken": csrf_token})
            
            return response

        return JsonResponse({"message": "Apenas email @cesar.school podem ser cadastrados"}, status=400)

    return JsonResponse({})
