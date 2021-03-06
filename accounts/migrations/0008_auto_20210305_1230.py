# Generated by Django 3.1.6 on 2021-03-05 09:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210304_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='card_name',
            field=models.CharField(default='KCB', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='card',
            field=models.ForeignKey(default='Please select an card', on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.card'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='netflix_account',
            field=models.ForeignKey(default='Please select an account', on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.netflix_account'),
        ),
        migrations.AlterField(
            model_name='income',
            name='netflix_account',
            field=models.ForeignKey(default='Please select an account', on_delete=django.db.models.deletion.SET_DEFAULT, to='accounts.netflix_account'),
        ),
    ]
