import json
import jwt
import pytz
from datetime import datetime, timedelta

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.conf import settings

from .models import CustomUser

@csrf_exempt
def getUser(req, email):
    if req.method == 'GET':
        try:
            user = CustomUser.objects.get(email=email)
            return JsonResponse({
                "id": user.id,
                "nome": user.first_name,
                "email": user.email,
                "image": user.image,
                "role": user.role,
            })
        except:
            return JsonResponse({'message': 'Usuário não encontrado'}, status=404)

    return JsonResponse({})


@csrf_exempt
def signUp(req):
    if req.method == 'POST':
        data = json.loads(req.body)

        name = data.get("nome")
        email = str(data.get("email"))
        image = data.get("image")

        if (email.endswith("@cesar.school")):
            user = CustomUser.objects.filter(email=email)

            if (len(user) >= 1):
                return JsonResponse({"message": "Usuário já existe"}, status=400)

            username = "_".join(name.split(" "))
            CustomUser.objects.create(
                email=email, image=image, username=username, first_name=name, role="aluno", password="inutilizável")

            response = JsonResponse(
                {"message": "Usuário criado com sucesso"})

            return response

        return JsonResponse({"message": "Apenas email @cesar.school podem ser cadastrados"}, status=400)

    return JsonResponse({})


@csrf_exempt
def get_csrftoken(req):
    if req.method == 'POST':
        csrf_token = get_token(req)
        return JsonResponse({"csrftoken": csrf_token})

    return JsonResponse({})


@csrf_exempt
def auth(req):
    if req.method == 'POST':
        data = json.loads(req.body)

        email: str = data.get("email")

        user = CustomUser.objects.filter(email=email)

        if (len(user) >= 1):
            user = user[0]
            utc_now = datetime.now(pytz.utc)
            payload = {
                'id': user.id,
                'email': email,
                'exp': utc_now + timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS),
                'iat': utc_now,
            }

            token = jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)

            return JsonResponse({"access": token})

    return JsonResponse({"message": "Usuário não existe"}, status=401)
