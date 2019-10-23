# Generated by Django 2.2.6 on 2019-10-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepaymentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied', models.BooleanField(default=False)),
                ('repaid', models.BooleanField(default=False)),
                ('monthly_repaid', models.BooleanField(default=False)),
                ('lateness', models.BooleanField(default=False)),
                ('loan_owed', models.DecimalField(decimal_places=3, max_digits=15, null=True)),
                ('paid_amount', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('per_monthly_payment', models.DecimalField(decimal_places=3, max_digits=15, null=True)),
                ('lateness_fee', models.DecimalField(decimal_places=3, max_digits=15, null=True)),
                ('max_loan_tenure', models.PositiveSmallIntegerField(null=True)),
                ('user_loan_tenure', models.PositiveSmallIntegerField(null=True)),
                ('next_payment_date', models.DateField(null=True)),
                ('lateness_date', models.DateField(null=True)),
                ('repayment_date', models.DateField(null=True)),
                ('loan_interest', models.IntegerField(null=True)),
                ('loan_disbursed', models.BooleanField(default=False)),
                ('user_loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanAccount')),
            ],
        ),
    ]
