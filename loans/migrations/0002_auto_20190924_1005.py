# Generated by Django 2.2.5 on 2019-09-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanaccount',
            name='disbursement_date',
            field=models.DateField(null=True),
        ),
    ]
