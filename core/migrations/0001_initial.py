# Generated by Django 2.2.6 on 2019-10-19 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField(verbose_name='Carga horária')),
                ('ementa', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('valor_hora_aula', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor hora/aula')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='Data de ínicio')),
                ('data_termino', models.DateField(verbose_name='Dat de término')),
                ('hora_inicio', models.TimeField(verbose_name='Horário do ínicio')),
                ('hora_termino', models.TimeField(verbose_name='Hórario do término')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor')),
            ],
        ),
    ]
