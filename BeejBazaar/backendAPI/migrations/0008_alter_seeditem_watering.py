# Generated by Django 3.2.8 on 2021-10-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0007_auto_20211022_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeditem',
            name='watering',
            field=models.CharField(max_length=64),
        ),
    ]