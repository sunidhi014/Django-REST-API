# Generated by Django 4.0.1 on 2022-01-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpotral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]