# Generated by Django 2.2.6 on 2019-10-25 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20191025_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanaccount',
            name='user_auth_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
