from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
import pandas as pd
from django.contrib import messages
from django.contrib.messages import constants
from django.http import JsonResponse
from .models import Aluno, Grupo, Fact
from .get_fact_grade import getMediaAluno, transformNotasToObject
from .get_students_excel import getStudents

class FeedBackView(View):
    def get(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        user = User.objects.get(username=req.user.username)
        groups = Grupo.objects.filter(professor=user)
        #dá append em grupos q foram compartilhados tbm

        context = {
            "user": user,
            "groups": groups
        }
        
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
        
        if(action == "addStudent"):
            return self.addStudent(req, context)
    
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
    
    def addStudent(self, req, context):
        file = None

        try:
            file = req.FILES["alunos"]
            df = pd.read_excel(file)

            getStudents(df)

        except Exception as e:
            print("exeption at 'addStudent' method - ", e)

        if(not file):
            matricula = req.POST.get("matricula")
            nome = req.POST.get("nome")
            email_school = req.POST.get("email-school")

            Aluno.objects.create(matricula=matricula, nome=nome, email=email_school)
        
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
        
        alunos = []

        for aluno in group[0].alunos.all():
            # filtra os facts pelo aluno e pelo grupo atual
            fact = list(filter(lambda x: x.grupo.nome == group[0].nome, list(aluno.fact_set.all())))
            sr1 = 0
            sr2 = 0

            if(len(list(fact)) == 1):
                # TODO REALIZAR CALCULO SR1
                #! O CALCULO ABAIXO ESTA SOMANDO APENAS O FACT
                sr1 = (
                    fact[0].pensamento_critico_criatividade + 
                    fact[0].comunicacao + 
                    fact[0].colaboracao + 
                    fact[0].qualidade_entregas + 
                    fact[0].presenca + 
                    fact[0].entrega_prazos
                )

            if(len(list(fact)) == 2):
                sr2 = (
                    fact[1].pensamento_critico_criatividade + 
                    fact[1].comunicacao + 
                    fact[1].colaboracao + 
                    fact[1].qualidade_entregas + 
                    fact[1].presenca + 
                    fact[1].entrega_prazos
                )

            alunos.append({
                "id": aluno.id,
                "nome": aluno.nome,
                "email": aluno.email,
                "sr1": round(sr1, 2),
                "sr2": round(sr2, 2),
                "media": round((sr1 + sr2) / 2, 2)
            })
        
        context = {
            "group": group[0],
            "alunos": alunos
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
                )

                fact = Fact.objects.create(
                    pensamento_critico_criatividade=aluno_object["pensamento_crítico_e_criatividade"],
                    comunicacao=aluno_object["comunicação"],
                    colaboracao=aluno_object["colaboração"],
                    qualidade_entregas=aluno_object["qualidade_das_entregas"],
                    presenca=aluno_object["presença"],
                    entrega_prazos=aluno_object["entregas_e_prazos"],
                    aluno=aluno,
                    grupo=group[0]
                )

                aluno.save()
                fact.save()

                group[0].alunos.add(aluno)
                group[0].save()

            else:
                group[0].alunos.add(aluno[0])
                group[0].save()

        return redirect("feedbackApp:group", id)


class deleteGroup(View):
    def get(self, req, groupId):
        #TODO: make it safe by verifying if group is indeed in user's range

        groupToDelete = Grupo.objects.get(id=groupId)
        groupToDelete.delete()
        return redirect("autenticacao:root")


class deleteAluno(View):
    def get(self, req, alunoId):
        #TODO: make it safe by verifying if aluno is indeed in user's range

        alunoToDelete = Aluno.objects.get(id=alunoId)
        alunoToDelete.delete()
        return redirect("autenticacao:root")


def delete_alunos(request, id):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        aluno_ids = data.get("ids", [])

        print("esse é o id: ", id)
        grupo = Grupo.objects.get(id=id)

        for aluno_id in aluno_ids:
            aluno = Aluno.objects.get(id=aluno_id)
            grupo.alunos.remove(aluno)
        
        return JsonResponse({"success": True})
    
def add_alunos(request, id):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        print("esse é o data: ", data)
        getMyGroup = data.get("group")
        print("esse é o value de getMyGroup", getMyGroup)
        myGroup = Grupo.objects.get(pk = getMyGroup)
        aluno_names_pra_add = data.get("names", []) # [] não é necessário, é um default value em casos onde não vem nada

        for aluno_name in aluno_names_pra_add:            
            
            aluno_novo, created = Aluno.objects.get_or_create(nome=aluno_name) #this ensures that we don't create an extra aluno if they already exist
            myGroup.alunos.add(aluno_novo)
            aluno_novo.save()
        
        return JsonResponse({"success": True})

def logoutFunction(req):
    logout(req)
    return redirect("autenticacao:root")

