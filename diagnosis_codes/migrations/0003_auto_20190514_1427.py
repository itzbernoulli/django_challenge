# Generated by Django 2.2.1 on 2019-05-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis_codes', '0002_auto_20190514_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosiscode',
            name='abbreviated_description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='diagnosiscode',
            name='category_title',
            field=models.CharField(max_length=255),
        ),
    ]