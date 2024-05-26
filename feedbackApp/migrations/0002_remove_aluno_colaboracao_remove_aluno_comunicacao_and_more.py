# Generated by Django 5.0.3 on 2024-05-26 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='colaboracao',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='comunicacao',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='entrega_prazos',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='pensamento_critico_criatividade',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='presenca',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='qualidade_entregas',
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='Status Report 1', max_length=255)),
                ('pensamento_critico_criatividade', models.FloatField(verbose_name='Pensamento Crítico e Criatividade')),
                ('comunicacao', models.FloatField(verbose_name='Comunicação')),
                ('colaboracao', models.FloatField(verbose_name='Colaboração')),
                ('qualidade_entregas', models.FloatField(verbose_name='Qualidade das Entregas')),
                ('presenca', models.FloatField(verbose_name='Presença')),
                ('entrega_prazos', models.FloatField(verbose_name='Entrega e Prazos')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbackApp.aluno')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbackApp.grupo')),
            ],
        ),
    ]
