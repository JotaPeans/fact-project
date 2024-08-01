from django.http.response import JsonResponse
from django.views import View
from .models import CustomUser
from django.contrib import auth

class User(View):
    def get(self, req):
        print(req)
        return JsonResponse({"id": "asd1kj23hjdjk12h3k12j"})


class SignUp(View):
    def post(self, req):
        id = req.POST.get("id")
        name = req.POST.get("name")
        email = str(req.POST.get("email"))
        image = req.POST.get("image")

        if(email.endswith("@cesar.school")):
            user = CustomUser.objects.filter(email=email)

            if(user[0]):
                return JsonResponse({"message": "Usuário já existe"}, status=400)
            
            CustomUser.objects.create(email=email, image=image, first_name=name, providerId=id, role="aluno")

            return JsonResponse({"message": "Usuário criado com sucesso"})
        
        return JsonResponse({"message": "Apenas email @cesar.school podem ser cadastrados"}, status=400)
