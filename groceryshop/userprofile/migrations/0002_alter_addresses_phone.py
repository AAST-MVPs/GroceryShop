# Generated by Django 4.2.8 on 2023-12-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
