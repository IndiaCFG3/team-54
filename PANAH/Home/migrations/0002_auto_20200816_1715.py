# Generated by Django 3.1 on 2020-08-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='state',
            field=models.CharField(choices=[('ANDHRA PRADESH', 'ANDHRA PRADESH'), ('TAMIL NADU', 'TAMIL NADU'), ('TELANGANA', 'TELANGANA'), ('MAHARASHTRA', 'MAHARASHTRA'), ('WEST BENGAL', 'WEST BENGAL'), ('UTTAR PRADESH', 'UTTAR PRADESH'), ('KARNATAKA', 'KARNATAKA'), ('KERALA', 'KERALA')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='schema',
            name='state',
            field=models.CharField(choices=[('ANDHRA PRADESH', 'ANDHRA PRADESH'), ('TAMIL NADU', 'TAMIL NADU'), ('TELANGANA', 'TELANGANA'), ('MAHARASHTRA', 'MAHARASHTRA'), ('WEST BENGAL', 'WEST BENGAL'), ('UTTAR PRADESH', 'UTTAR PRADESH'), ('KARNATAKA', 'KARNATAKA'), ('KERALA', 'KERALA')], default='1', max_length=20),
        ),
    ]