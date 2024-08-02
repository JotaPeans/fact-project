from django.contrib import admin
from .models import Aluno, Grupo, Fact

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Fact)
admin.site.register(Grupo)