# Generated by Django 4.0.4 on 2022-05-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crifForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_i_code', models.CharField(max_length=5, verbose_name='Financial Institution Code - XXXXX')),
                ('branch_code', models.CharField(max_length=7, verbose_name='Branch Code - BRANCH00')),
                ('last_acc_date', models.DateField(max_length=8, verbose_name='Last Accounting Date - DDMMYYYY - 00000000')),
                ('date_of_prod', models.DateField(auto_now_add=True, verbose_name='Production Date - 00000000')),
                ('code', models.IntegerField(verbose_name='Code - 000')),
                ('corr_flag', models.CharField(max_length=1, verbose_name="Correction flag - '1' or ' '")),
                ('contract_columns', models.FileField(upload_to='uploads/', verbose_name="Submit 'CRIFCONTRACTDATA.xlsx' File Here")),
                ('subject_columns', models.FileField(upload_to='uploads/', verbose_name="Submit 'CRIFSUBJECTDATA.xlsx' File Here")),
            ],
            options={
                'db_table': 'client',
            },
        ),
    ]
