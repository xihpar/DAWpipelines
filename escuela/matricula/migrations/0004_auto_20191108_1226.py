# Generated by Django 2.2.5 on 2019-11-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_auto_20191108_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso',
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ManyToManyField(null=True, to='matricula.Curso'),
        ),
    ]