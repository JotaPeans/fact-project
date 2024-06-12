from django.contrib import admin
from .models import Aluno, Grupo, Fact, GoogleCredentials

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Fact)
admin.site.register(Grupo)
admin.site.register(GoogleCredentials)