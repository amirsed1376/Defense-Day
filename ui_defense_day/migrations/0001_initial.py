# Generated by Django 3.0.1 on 2019-12-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('role', models.CharField(choices=[('student', 'Student'), ('presenter', 'Presenter'), ('industry', 'Industry'), ('supervisor', 'Supervisor'), ('referee', 'Referee')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
            },
        ),
    ]