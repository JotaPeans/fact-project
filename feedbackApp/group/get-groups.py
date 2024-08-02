from ..models import Grupo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def get_groups(req):
  if(req.method == 'GET'):
    ...
  return JsonResponse({}, status=405)