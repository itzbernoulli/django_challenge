# Generated by Django 2.2.1 on 2019-05-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(max_length=4)),
                ('diagnosis_code', models.CharField(max_length=5)),
                ('full_code', models.CharField(max_length=7)),
                ('abbreviated_description', models.CharField(max_length=100)),
                ('full_description', models.CharField(max_length=255)),
                ('category_title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
