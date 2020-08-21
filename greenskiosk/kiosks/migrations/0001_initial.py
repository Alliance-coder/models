# Generated by Django 3.1 on 2020-08-21 11:28

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
            name='KioskOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('id_number', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
                ('date_opened', models.DateField()),
                ('street_address', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=8)),
                ('phone_number', models.IntegerField()),
                ('business_type', models.CharField(max_length=28)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiosks.kioskowner')),
            ],
        ),
    ]