import re

typeNotas = [
    "Pensamento Crítico e Criatividade", 
    "Comunicação", 
    "Colaboração", 
    "Qualidade das Entregas", 
    "Presença", 
    "Entregas e Prazos"
]

alunos = {}

def alunoAtualInAlunos(aluno):
    for index in alunos:
        if(aluno in alunos[index]):
            return True
        
    return False;

def getAlunoEmail(aluno):
    for _, valor in alunos.items():
        if valor[1] == aluno:
            return valor[0]
        
    return ""

reject = [
    "Carimbo de data/hora", 
    "Endereço de e-mail", 
    "Nome completo"
]


def getMediaAluno(df):
    notas = []

    for nome_coluna in df.columns:
        for index, x in enumerate(df[nome_coluna]):
            if(nome_coluna == "Endereço de e-mail"):
                alunos[index] = [x]
            if(nome_coluna == "Nome completo"):
                alunos[index].append(x)

    for nome_coluna in df.columns:
        match = re.search(r'\(([^)]*)\)', nome_coluna)
        tipoNota = re.sub(r'\s+\([^)]*\)', '', nome_coluna)
        
        if(match):
            aluno_atual = match.group(1)

            somaNotas = 0
            countNotas = 0
            media = 0

            for index, x in enumerate(df[nome_coluna]):
                if(nome_coluna not in reject and not nome_coluna.startswith("Justifique suas respostas")):

                    nota = x
                    
                    if(aluno_atual in alunos[index]):
                        nota = 0
                    
                    somaNotas += nota
                    countNotas += 1
                
                else:
                    somaNotas += 0
                    countNotas += 1

            media = somaNotas / (countNotas - 1)

            if(not alunoAtualInAlunos(aluno_atual)):
                media = 0

            notas.append([ aluno_atual, getAlunoEmail(aluno_atual), tipoNota, media ])

    return notas


def transformNotasToObject(notas: list):
    objeto = {
        "nome": notas[0][0],
        "email": notas[0][1]
    }

    for array in notas:
        atributo = array[2].lower().replace(' ', '_')
        objeto[atributo] = array[3]

    return objeto