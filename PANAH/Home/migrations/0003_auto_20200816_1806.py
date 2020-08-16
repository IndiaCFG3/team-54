# Generated by Django 3.1 on 2020-08-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200816_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='organization',
            field=models.CharField(choices=[('1', 'Organised '), ('2', 'UnOrganised'), ('3', 'Other')], default='Organised', max_length=20),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other')], default='Female', max_length=20),
        ),
        migrations.AlterField(
            model_name='enduser',
            name='state',
            field=models.CharField(choices=[('ANDHRA PRADESH', 'ANDHRA PRADESH'), ('TAMIL NADU', 'TAMIL NADU'), ('TELANGANA', 'TELANGANA'), ('MAHARASHTRA', 'MAHARASHTRA'), ('WEST BENGAL', 'WEST BENGAL'), ('UTTAR PRADESH', 'UTTAR PRADESH'), ('KARNATAKA', 'KARNATAKA'), ('KERALA', 'KERALA')], default='Andhra Pradesh', max_length=20),
        ),
    ]