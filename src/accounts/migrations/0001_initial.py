# Generated by Django 2.2.4 on 2019-08-30 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Pic', models.ImageField(upload_to='img/')),
                ('country_code', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
