# Generated by Django 2.2.6 on 2020-01-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0009_auto_20200105_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolecoefficent',
            name='job',
            field=models.CharField(choices=[('student', 'Student'), ('industry', 'Industry'), ('supervisor', 'Supervisor'), ('professor', 'Professor')], max_length=20, unique=True),
        ),
    ]
