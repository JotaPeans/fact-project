from pandas import DataFrame

from .models import Aluno

def getStudents(df: DataFrame):
    for row in range(len(df)):
        aluno = {}
        for nome_coluna in df.columns:
            for index, x in enumerate(df[nome_coluna]):
                if(index == row):
                    aluno[nome_coluna] = x
        
        try:
            Aluno.objects.get(matricula=aluno["ALUNO"])
        except:
            Aluno.objects.create(nome=aluno["NOME_ALUNO"], email=aluno["MAILBOX"], matricula=aluno["ALUNO"], turma=aluno["TURMA_PREF"])
