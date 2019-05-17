# Generated by Django 2.2.1 on 2019-05-16 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=1024, unique=True, verbose_name='Full name')),
                ('street_name', models.CharField(max_length=1024, verbose_name='Street name')),
                ('suburb', models.CharField(max_length=1024, verbose_name='Suburb')),
                ('postcode', models.CharField(max_length=6, verbose_name='Postcode')),
                ('state', models.CharField(max_length=1024, verbose_name='State')),
                ('client_contact_name', models.CharField(max_length=1024, unique=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]