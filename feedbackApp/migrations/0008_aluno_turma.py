# Generated by Django 5.0.3 on 2024-06-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackApp', '0007_grupo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.CharField(default='', max_length=50),
        ),
    ]
