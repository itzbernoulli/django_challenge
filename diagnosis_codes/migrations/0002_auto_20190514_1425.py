# Generated by Django 2.2.1 on 2019-05-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis_codes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosiscode',
            name='category_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='diagnosiscode',
            name='diagnosis_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='diagnosiscode',
            name='full_code',
            field=models.CharField(max_length=10),
        ),
    ]
