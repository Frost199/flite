# Generated by Django 2.1.9 on 2021-06-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210607_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Successful', 'SUCCESSFUL'), ('Failed', 'FAILED'), ('Canceled', 'CANCELED')], default='Successful', help_text='status of transaction performed', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('Bank Transaction', 'BANK_TRANSACTION'), ('Deposit', 'DEPOSIT'), ('Withdraw', 'WITHDRAW'), ('Peer To Peer', 'PEER_TO_PEER')], help_text='type of transaction performed', max_length=100, null=True),
        ),
    ]
