# Generated by Django 5.0.3 on 2024-06-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackApp', '0002_remove_aluno_colaboracao_remove_aluno_comunicacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
