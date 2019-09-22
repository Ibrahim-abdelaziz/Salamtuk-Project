# Generated by Django 2.2.4 on 2019-09-02 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_app', '0003_booking_days_of_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paitent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Birth_of_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Check_times',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Days_of_work',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Doctor',
        ),
        migrations.AddField(
            model_name='booking',
            name='doctor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_id', to='doctors_app.Doctor'),
        ),
        migrations.CreateModel(
            name='Appoientment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoientment_day', models.CharField(choices=[('saturday', 'saturday'), ('sunday', 'sunday'), ('monday', 'monday'), ('tuseday', 'tuseday'), ('wensday', 'wensday'), ('thursday', 'thursday'), ('friday', 'friday')], max_length=250)),
                ('appoientment_time', models.CharField(default='From:   To:  ', max_length=250)),
                ('name_of_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to='doctors_app.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='Appoientment_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Appoientment', to='doctors_app.Appoientment'),
        ),
        migrations.AddField(
            model_name='booking',
            name='Patient_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Paitent', to='doctors_app.Paitent'),
        ),
    ]
