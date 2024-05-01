from googleapiclient.discovery import build
from google.oauth2 import service_account

CREDENTIALS_PATH = "./credentials.json"

SCOPES_FORMS = ["https://www.googleapis.com/auth/forms.body"]
SCOPES_DRIVE = ["https://www.googleapis.com/auth/drive"]

descricao_fact = '''No uso do FACT, os membros do time atribuem notas individuais (exceto a si próprios), tomando como referência os Critérios de Avaliação.

São Avaliados os seguintes critérios:

    1. Pensamento Crítico e Criatividade;
    2. Comunicação;
    3. Colaboração;
    4. Qualidade das Entregas;
    5. Presença;
    6. Entregas e Prazos.


Os critérios 1, 2, 3 e 4 valem, cada um deles, de 0 a 20 pontos. Já os critérios 5 e 6, valem de 0 a 10 pontos, cada um deles, totalizando 100 pontos caso o integrante alcance a nota máxima em todos os critérios. Essa pontuação será referente a porcentagem da nota obtida pelo grupo em cada Status Report.

Ao atribuir qualquer nota entre 1 e 9, não anteceder o número com "0" (zero). Por exemplo, dar nota "7", NÃO "07".

Lembre-se, o somatório das notas atribuídas aos seus colegas de time não deve ultrapassar a quantidade de PONTOS informado em cada critério. 

O FACT não contempla autoavaliação, portanto ao chegar em sua própria avaliação, o estudante deverá colocar "0" (zero) em todas as notas, e justificar dizendo "sou eu".'''



credentials_forms = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES_FORMS)
credentials_drive = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES_DRIVE)

service = build("forms", "v1", credentials=credentials_forms)

drive_service = build("drive", "v3", credentials=credentials_drive)


def add_permission(file_id: str, email_address: str):
    permission = {
        "type": "user",
        "role": "writer",
        "emailAddress": email_address
    }

    try:
        drive_service.permissions().create(
            fileId=file_id,
            body=permission,
            fields="id"
        ).execute()

    except Exception as e:
        print("error: ", e)



alunos = ["ADRIANA SOUZA LIMA","ALBERTO CARVALHO SANTOS","ALESSANDRA PEREIRA SILVA","ALEXANDRE COSTA BARBOSA","ALICE FERREIRA GOMES","AMANDA ALVES RIBEIRO","ANA BEATRIZ CASTRO OLIVEIRA","ANA CAROLINA MORAES ROCHA","ANDRÉ LUIZ CARDOSO ALMEIDA","ANTÔNIO CARLOS BATISTA MARTINS","ARIANE CUNHA MELO","BRUNA SOUZA SANTOS","BRUNO HENRIQUE LIMA FERREIRA"]

title_images = [
    {
        "title": "Pensamento Crítico e Criatividade",
        "image": "https://i.imgur.com/xNaDpoc.png"
    },
    {
        "title": "Comunicação",
        "image": "https://i.imgur.com/Tjhel7A.png"
    },
    {
        "title": "Colaboração",
        "image": "https://i.imgur.com/hbXn70n.png"
    },
    {
        "title": "Qualidade das Entregas",
        "image": "https://i.imgur.com/dPtDaLx.png"
    },
    {
        "title": "Presença",
        "image": "https://i.imgur.com/71kxBpq.png"
    },
    {
        "title": "Entregas e Prazos",
        "image": "https://i.imgur.com/HGmKO8V.png"
    },
    {
        "title": "Justifique suas respostas",
        "image": ""
    },
]

def create_new_form(lista_perguntas):
    form = {
        "info": {
            "title": "FACT - Fator de Contribuição Técnica",
        }
    }
    created_form = service.forms().create(body=form).execute()

    formId = created_form["formId"]

    updates = {
        "requests": lista_perguntas
    }

    service.forms().batchUpdate(formId=formId, body=updates).execute()

    add_permission(formId, "apabs@gmail.com") #esse email corresponde a permissão para editar o forms. Ou seja, o email do professor fica aqui.

    print(f"URL for {aluno}'s form: https://docs.google.com/forms/d/{formId}")


def create_item(title, aluno, image, count):
    if(image):
        return {
            "createItem": {
                "item": {
                    "title": f"{title} ({aluno})",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "textQuestion": {
                                "paragraph": False
                            }
                        },
                        "image": {
                            "sourceUri": image
                        }
                    }
                },
                "location": {
                    "index": count
                }
            },
        }
    else:
        return {
            "createItem": {
                "item": {
                    "title": f"{title} ({aluno})",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "textQuestion": {
                                "paragraph": False
                            }
                        }
                    }
                },
                "location": {
                    "index": count
                }
            },
        }


def create_page_break(title, count):
    return {
        "createItem": {
            "item": {
                "title": title,
                "pageBreakItem": {},
            },
            "location": {
                "index": count
            }
        }
    }


def update_form_info():
    return {
        "updateFormInfo": {
            "info": {
                "title": "FACT - Fator de Contribuição Técnica",
                "description": descricao_fact
            },
            "updateMask": "*"
        }
    }


for aluno in alunos:
    count = 0
    lista_perguntas = []
    alunosSemAlunoAtual = filter(lambda x: x != aluno, alunos)

    lista_perguntas.append(update_form_info())

    for other_student in alunosSemAlunoAtual:
        lista_perguntas.append(create_page_break(count=count, title=other_student))
        count += 1

        for title_images_index in range(7):
            question_item = create_item(
                aluno=other_student, 
                count=count, 
                title=title_images[title_images_index]["title"], 
                image=title_images[title_images_index]["image"]
            )
            
            lista_perguntas.append(question_item)
            count += 1

    create_new_form(lista_perguntas)

