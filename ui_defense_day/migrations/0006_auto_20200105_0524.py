# Generated by Django 2.2.6 on 2020-01-05 05:24

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_defense_day', '0005_auto_20200105_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
    ]