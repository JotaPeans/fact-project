import pandas as pd
import json
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages import constants
from django.http import JsonResponse

from .create_fact import Fact as FactClass
from .models import Aluno, Grupo, Fact, GoogleCredentials
from .get_fact_grade import getMediaAluno, transformNotasToObject
from .get_students_excel import getStudents

class FeedBackView(View):
    def get(self, req):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        user = User.objects.get(username=req.user.username)

        allowed_groups = []

        groups = Grupo.objects.all()
        for group in groups:
            professors = list(group.sharedToProfessor.all())

            if(group.professor.email == user.email):
                allowed_groups.append(group)

            else:
                for professor in professors:
                    if(user == professor):
                        allowed_groups.append(group)
        
        all_users = list(User.objects.all())
        users_to_list = []

        for current_user in all_users:
            if(current_user == user):
                continue
            else:
                users_to_list.append(current_user)

        #dá append em grupos q foram compartilhados tbm

        context = {
            "user": user,
            "groups": allowed_groups,
            "allUsers": users_to_list
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
            return self.addStudent(req)
    
    def addGroup(self, req, context, user):
        groupName = req.POST.get("groupName")

        if(len(groupName) < 5):
            groups = Grupo.objects.filter(professor=user)

            context["groups"] = groups

            messages.add_message(req, constants.ERROR, 'O nome do grupo precisa ter no mínimo 5 caracteres!')

            return render(req, "feedbackApp/app.html", context=context)
        
        group = Grupo.objects.create(nome=groupName, professor=context["user"])
        group.save()

        return redirect("feedbackApp:root")
    
    def addStudent(self, req):
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
            turma = req.POST.get("turma")

            Aluno.objects.create(matricula=matricula, nome=nome, email=email_school, turma=turma)
        
        return redirect("feedbackApp:root")
    
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
            fact = list(filter(lambda x: x.grupo.nome == group[0].nome, list(aluno.fact_set.all())))
            sr1 = 0
            sr2 = 0

            if(len(list(fact)) == 1):
                sr1 = (
                    fact[0].pensamento_critico_criatividade + 
                    fact[0].comunicacao + 
                    fact[0].colaboracao + 
                    fact[0].qualidade_entregas + 
                    fact[0].presenca + 
                    fact[0].entrega_prazos
                )

            if(len(list(fact)) == 2):
                sr1 = (
                    fact[0].pensamento_critico_criatividade + 
                    fact[0].comunicacao + 
                    fact[0].colaboracao + 
                    fact[0].qualidade_entregas + 
                    fact[0].presenca + 
                    fact[0].entrega_prazos
                )

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
                "matricula": aluno.matricula,
                "sr1": round(sr1, 2),
                "sr2": round(sr2, 2),
                "media": round((sr1 + sr2) / 2, 2)
            })

        todosAlunos = Aluno.objects.all()
        context = {
            "group": group[0],
            "alunos": alunos,
            "todosAlunos": todosAlunos
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

        except Exception as e:
            print(e)
            messages.add_message(req, constants.ERROR, 'Excel ou arquivo no formato inválido')
            return render(req, "feedbackApp/group.html", context=context)

        alunos = []
        
        for nome_aluno, *_ in notas:
            if(nome_aluno not in alunos):
                alunos.append(nome_aluno)

        for nome_aluno in alunos:
            aluno_data = list(filter(lambda x: x[0] == nome_aluno, notas))

            aluno_object = transformNotasToObject(aluno_data)
            
            aluno = Aluno.objects.filter(nome=aluno_object["nome"])[0]
            alunoFacts = len(aluno.fact_set.all())

            if(aluno):
                fact = Fact.objects.create(
                    nome="Status Report 1" if alunoFacts == 0 else "Status Report 2",
                    pensamento_critico_criatividade=aluno_object["pensamento_crítico_e_criatividade"],
                    comunicacao=aluno_object["comunicação"],
                    colaboracao=aluno_object["colaboração"],
                    qualidade_entregas=aluno_object["qualidade_das_entregas"],
                    presenca=aluno_object["presença"],
                    entrega_prazos=aluno_object["entregas_e_prazos"],
                    aluno=aluno,
                    grupo=group[0]
                )

                fact.save()

        return redirect("feedbackApp:group", id)


class GroupStudent(View):
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
                "matricula": aluno.matricula,
                "sr1": round(sr1, 2),
                "sr2": round(sr2, 2),
                "media": round((sr1 + sr2) / 2, 2)
            })
        

        todosAlunos = list(Aluno.objects.all())
        alunos_desg = [aluno for aluno in todosAlunos if aluno.turma.startswith("DESG")]
        alunos_comp = [aluno for aluno in todosAlunos if aluno.turma.startswith("COMP")]

        # alunosCC = 
        context = {
            "group": group[0],
            "alunos": alunos,
            "todosAlunos": todosAlunos,
            "alunosCC": alunos_comp,
            "alunosDESIGN": alunos_desg,
        }
        
        return render(req, "feedbackApp/alunos-grupo.html", context=context)
    
    def post(self, req, id):
        if(not req.user.is_authenticated):
            return redirect("autenticacao:root")
        
        alunos = json.loads(req.body)["alunos"]

        try:
            grupo = Grupo.objects.get(pk=id)

            alunos = [Aluno.objects.get(pk=aluno.split("::")[0]) for aluno in alunos]

            grupo.alunos.set(alunos)
            
            return JsonResponse({"message": "Alunos alterados com sucesso!"})
        except Exception as e:
            return JsonResponse({"message": f"Erro: {e}"}, status=400)
    
class deleteGroup(View):
    def get(self, req, groupId):
        #TODO: make it safe by verifying if group is indeed in user's range

        groupToDelete = Grupo.objects.get(id=groupId)
        groupToDelete.delete()
        return redirect("autenticacao:root")


class AlunoEdit(View):
    def post(self, req):
        if(not req.user.is_authenticated):
            return JsonResponse({"message": "Não autenticado"})
        
        alunoId = req.POST.get("alunoId")
        nome = req.POST.get("nome")
        email = req.POST.get("email")
        matricula = req.POST.get("matricula")
        groupId = req.POST.get("groupId")

        try:
            aluno = Aluno.objects.get(pk=alunoId)

            aluno.nome = nome
            aluno.email = email
            aluno.matricula = matricula

            aluno.save()

            return redirect("feedbackApp:group", id=groupId)
            
        except:
            return redirect("feedbackApp:group", id=groupId)


class FactCreate(View):
    def post(self, req, groupId):
        if(not req.user.is_authenticated):
            return JsonResponse({"message": "Não autenticado"})
        
        try:
            grupo = Grupo.objects.get(pk=groupId)

            alunos = list(grupo.alunos.all())

            alunos_nomes = [aluno.nome for aluno in alunos]
            alunos_emails = [aluno.email for aluno in alunos]

            fact = FactClass()

            fact = fact.create_fact(email_address=req.user.email, alunos=alunos_nomes, emails=alunos_emails)

            if(fact["error"] == None):
                return JsonResponse({ "url": fact["formUrl"] })
            
            else:
                raise Exception(fact["error"])

        except Exception as e:
            return JsonResponse({ "message": f"Erro: {e}" }, status=400)


def getAlunos(req, id):
    if(not req.user.is_authenticated):
        return JsonResponse({"message": "Não autenticado"})
    
    if(req.method == "GET"):
        try:
            group = Grupo.objects.get(pk=id)

            alunos = [{
                "id": aluno.id,
                "nome": aluno.nome,
                "turma": aluno.turma
            } for aluno in list(group.alunos.all())]

            return JsonResponse({ "alunos": alunos })
        except Exception as e:
            return JsonResponse({ "message": f"Erro {e}" }, status=400)
    
def addAdmin(req):
    if(not req.user.is_authenticated):
        return JsonResponse({"message": "Não autenticado"})
    
    if req.method == "POST": # ({ professorEscolhido: valorEscolhido, group: groupId})
        data = json.loads(req.body)
        getMyGroup = data.get("group")
        professorEscolhido = data.get("professorEscolhido")

        myGroup = Grupo.objects.get(pk=getMyGroup)
        myGroup.sharedToProfessor.add(professorEscolhido)
        return JsonResponse({"success": True})
    
def changeAlunoInfo(req):
    if(not req.user.is_authenticated):
        return JsonResponse({"message": "Não autenticado"})
    
    if req.method == "POST":
        data = json.loads(req.body)
        getMyAlunoId = data.get("alunoId")
        getMyGroupId = data.get("idDoGrupo")
        
        aluno = Aluno.objects.get(id = getMyAlunoId)
        print("achei o aluno, sua matricula é: ", aluno.matricula)


        aluno.nome = data.get("novoNomeDoAluno")
        aluno.email = data.get("novoEmailDoAluno")
        aluno.matricula = data.get("novaMatriculaDoAluno")
        aluno.save()
        return JsonResponse({"success": True})

