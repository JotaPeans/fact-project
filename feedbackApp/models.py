from django.db import models
from autenticacao.models import CustomUser

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    matricula = models.CharField(max_length=15, default="")
    turma = models.CharField(max_length=50, default="")

    def __str__(self) -> str:
        return self.nome
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'matricula': self.matricula,
            'turma': self.turma
        }
    

class Grupo(models.Model):
    nome = models.CharField(max_length=200)  
    alunos = models.ManyToManyField(Aluno, related_name='grupos')
    professor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sharedToProfessor = models.ManyToManyField(CustomUser, related_name='professoresAdmins')
    image = models.CharField(max_length=200, default = 'a')

    def __str__(self) -> str:
        return self.nome
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'alunos': [aluno.to_dict() for aluno in self.alunos.all()],
            'professor': self.professor.to_dict(),
            'sharedToProfessor': [shared.to_dict() for shared in self.sharedToProfessor.all()],
            'image': self.image,
        }


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
    
    def to_dict(self):
        return {
            'id': self.id,
            'aluno': self.aluno.to_dict(),
            'grupo': self.grupo.to_dict(),
            'nome': self.nome,
            'pensamento_critico_criatividade': self.pensamento_critico_criatividade,
            'comunicacao': self.comunicacao,
            'colaboracao': self.colaboracao,
            'qualidade_entregas': self.qualidade_entregas,
            'presenca': self.presenca,
            'comunicacao': self.comunicacao,
            'entrega_prazos': self.entrega_prazos
        }