# Generated by Django 2.2 on 2019-12-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0002_presenter_file2'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenter',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]