# Generated by Django 3.1.6 on 2021-02-26 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='initial_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='card',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='initial_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='netflix_account',
            name='initial_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='netflix_account',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]