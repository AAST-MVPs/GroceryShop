# Generated by Django 4.2.8 on 2023-12-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('F', 'Fulfilled'), ('U', 'Unfulfilled'), ('C', 'Canceled'), ('R', 'Refunded')], default='F'),
        ),
    ]
