# Generated by Django 3.2.8 on 2021-10-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0002_auto_20211022_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeditem',
            name='title',
            field=models.CharField(default='Seed', max_length=32),
        ),
    ]
