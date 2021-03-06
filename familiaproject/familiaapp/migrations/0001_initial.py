# Generated by Django 4.0.4 on 2022-06-20 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.CharField(default=uuid.UUID('ef39aa9b-e51a-4e61-98f2-9d50b5bf517b'), max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('cumpleaños', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Menues',
            fields=[
                ('id', models.CharField(default=uuid.UUID('1f791688-7083-40af-8ef1-51752e1ad8b2'), max_length=100, primary_key=True, serialize=False)),
                ('menue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesa', models.IntegerField()),
                ('invitacion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
