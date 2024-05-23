from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Aluno, Grupo
from .functions import getMediaAluno, transformNotasToObject
import pandas as pd
from django.contrib import messages
from django.contrib.messages import constants
from django.http import JsonResponse

class FeedBackView(View):
    def get(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        user = User.objects.get(username=req.user.username)
        groups = Grupo.objects.filter(professor=user)

        context = {
            "user": user,
            "groups": groups
        }
        print(f"groups de context é: {context['groups']}")
        
        return render(req, "feedbackApp/app.html", context=context)


    def post(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        action = req.POST.get("action")

        user = User.objects.get(username=req.user.username)
        
        context = {
            "user": user
        }

        if(action == "addGroup"):
            return self.addGroup(req, context, user)
        #if(action =="removeGroup"):
        #    id = Group.objects.get(id=pk)
        #    return self.deleteGroup(req,context,user,id)

    
    def addGroup(self, req, context, user):
        groupName = req.POST.get("groupName")

        if(len(groupName) < 5):
            groups = Grupo.objects.filter(professor=user)

            context["groups"] = groups

            messages.add_message(req, constants.ERROR, 'O nome do grupo precisa ter no mínimo 5 caracteres!')

            return render(req, "feedbackApp/app.html", context=context)
        
        group = Grupo.objects.create(nome=groupName, professor=context["user"])
        group.save()

        groups = Grupo.objects.filter(professor=user)

        context["groups"] = groups

        return render(req, "feedbackApp/app.html", context=context)
    
    def deleteGroup(self,req,context,user,id):
        group_to_delete = Grupo.objects.get(id=id)
        group_to_delete.delete()
    




class GroupView(View):
    def get(self, req, id):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        group = Grupo.objects.filter(pk=id)

        if(not group.exists()):
            return redirect("feedbackApp:root")
        
        context = {
            "group": group[0],
            "alunos": group[0].alunos.all()
        }
        
        return render(req, "feedbackApp/group.html", context=context)
    

    def post(self, req, id):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        group = Grupo.objects.filter(pk=id)

        if(not group.exists()):
            return redirect("feedbackApp:root")
        
        context = {
            "group": group[0]
        }

        try:
            file = req.FILES["file"]
            df = pd.read_excel(file)

            notas = getMediaAluno(df)

        except:
            messages.add_message(req, constants.ERROR, 'Excel ou arquivo no formato inválido')
            return render(req, "feedbackApp/group.html", context=context)

        alunos = []
        
        for nome_aluno, *_ in notas:
            if(nome_aluno not in alunos):
                alunos.append(nome_aluno)

        for nome_aluno in alunos:
            aluno_data = list(filter(lambda x: x[0] == nome_aluno, notas))

            aluno_object = transformNotasToObject(aluno_data)
            
            aluno = Aluno.objects.filter(nome=aluno_object["nome"])

            if(not aluno.exists()):

                aluno = Aluno.objects.create(
                    nome=aluno_object["nome"],
                    email=aluno_object["email"],
                    pensamento_critico_criatividade=aluno_object["pensamento_crítico_e_criatividade"],
                    comunicacao=aluno_object["comunicação"],
                    colaboracao=aluno_object["colaboração"],
                    qualidade_entregas=aluno_object["qualidade_das_entregas"],
                    presenca=aluno_object["presença"],
                    entrega_prazos=aluno_object["entregas_e_prazos"]
                )

                aluno.save()

                group[0].alunos.add(aluno)
                group[0].save()

            else:
                group[0].alunos.add(aluno[0])
                group[0].save()

        group = Grupo.objects.get(pk=id)

        context["alunos"] = group.alunos.all()

        return render(req, "feedbackApp/group.html", context=context)


class deleteGroup(View):
    def get(self, req, groupId):
        #TODO: make it safe by verifying if group is indeed in user's range

        groupToDelete = Grupo.objects.get(id=groupId)
        groupToDelete.delete()
        return redirect("autenticacao:root")

class deleteAluno(View):
    def get(self,alunoId, req):
        #TODO: make it safe by verifying if alumni is indeed in user's range

        alumniToDelete = Aluno.objects.get(id=alunoId)
        alumniToDelete.delete()
        return redirect("autenticacao:root")
class Group(View):
    def get(self, req, id):
        if(not req.user.is_authenticated):
            return JsonResponse({"message": "Unauthorized"}, status=401)
        
        group = Grupo.objects.filter(pk=id)

        if(not group.exists()):
            return JsonResponse({"message": "Grupo não existe"}, status=404)
        
        alunos = group[0].alunos.all()

        data = {
            'group': list(group.values()),
            'alunos': list(alunos.values())
        }
        return JsonResponse(data)


def logoutFunction(req):
    logout(req)
    return redirect("autenticacao:root")
