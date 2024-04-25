from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Aluno, Grupo
from .functions import getMediaAluno, transformNotasToObject
import pandas as pd

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

    
    def addGroup(self, req, context, user):
        groupName = req.POST.get("groupName")
        
        group = Grupo.objects.create(nome=groupName, professor=context["user"])
        group.save()

        groups = Grupo.objects.filter(professor=user)

        context["groups"] = groups

        return render(req, "feedbackApp/app.html", context=context)


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

        #! TODO FAZER VERIFICACAO SE O ARQUIVO PERTENCE A ESSES TIPOS DE APPLICATION:
        #! "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        #! ou
        #! "application/vnd.ms-excel" 

        file = req.FILES["file"]
        df = pd.read_excel(file)

        notas = getMediaAluno(df)

        alunos = []
        
        for nome_aluno, *_ in notas:
            if(nome_aluno not in alunos):
                alunos.append(nome_aluno)

        for nome_aluno in alunos:
            aluno_data = list(filter(lambda x: x[0] == nome_aluno, notas))

            aluno_object = transformNotasToObject(aluno_data)

            # print(aluno_object)
            
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

        group = Grupo.objects.get(pk=id)

        context["alunos"] = group.alunos.all()

        return render(req, "feedbackApp/group.html", context=context)

def logoutFunction(req):
    logout(req)
    return redirect("autenticacao:root")
        