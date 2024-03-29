# Generated by Django 3.1 on 2020-08-16 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('income_max', models.IntegerField()),
                ('income_min', models.IntegerField()),
                ('state', models.CharField(choices=[('1', 'ANDHRA PRADESH'), ('2', 'TAMIL NADU'), ('3', 'TELANGANA'), ('4', 'MAHARASHTRA'), ('5', 'WEST BENGAL'), ('6', 'UTTAR PRADESH'), ('7', 'KARNATAKA'), ('8', 'KERALA')], default='1', max_length=20)),
                ('max_fam', models.IntegerField()),
                ('min_fam', models.IntegerField()),
                ('living', models.CharField(choices=[('1', 'OWN HOUSE'), ('2', 'RENT'), ('3', 'Other')], default='1', max_length=20)),
                ('organization', models.CharField(choices=[('1', 'Organised '), ('2', 'UnOrganised'), ('3', 'Other')], default='1', max_length=20)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('location', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
                ('income', models.IntegerField()),
                ('family_size', models.IntegerField()),
                ('address', models.TextField()),
                ('pin_code', models.IntegerField()),
                ('state', models.CharField(choices=[('1', 'ANDHRA PRADESH'), ('2', 'TAMIL NADU'), ('3', 'TELANGANA'), ('4', 'MAHARASHTRA'), ('5', 'WEST BENGAL'), ('6', 'UTTAR PRADESH'), ('7', 'KARNATAKA'), ('8', 'KERALA')], default='1', max_length=20)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other')], default='1', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=20)),
                ('ngo_id', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
