# Generated by Django 3.1.6 on 2021-03-05 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210305_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='netflix_account',
            field=models.ForeignKey(default='Please select an account', on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.netflix_account'),
        ),
        migrations.AlterField(
            model_name='netflix_account',
            name='card',
            field=models.ForeignKey(default='Please select a card', on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.card'),
        ),
    ]
