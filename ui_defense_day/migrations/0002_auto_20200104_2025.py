# Generated by Django 2.2.6 on 2020-01-04 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='presenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui_defense_day.Presenter'),
        ),
        migrations.AlterField(
            model_name='score',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Score_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
