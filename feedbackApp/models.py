from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    matricula = models.CharField(max_length=15, default="")
    

    def __str__(self) -> str:
        return self.nome
    

class Grupo(models.Model):
    nome = models.CharField(max_length=200)  
    alunos = models.ManyToManyField(Aluno, related_name='grupos')
    professor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome


class Fact(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    nome = models.CharField(max_length=255, default="Status Report 1")
    pensamento_critico_criatividade = models.FloatField(verbose_name="Pensamento Crítico e Criatividade")
    comunicacao = models.FloatField(verbose_name="Comunicação")
    colaboracao = models.FloatField(verbose_name="Colaboração")
    qualidade_entregas = models.FloatField(verbose_name="Qualidade das Entregas")
    presenca = models.FloatField(verbose_name="Presença")
    entrega_prazos = models.FloatField(verbose_name="Entrega e Prazos")

    def __str__(self) -> str:
        return self.nome + " - " + self.aluno.nome