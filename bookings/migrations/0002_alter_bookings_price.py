# Generated by Django 5.0 on 2024-01-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]