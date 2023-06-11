# Generated by Django 4.2.1 on 2023-06-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_alter_location_latitud_alter_location_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitud',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitud',
            field=models.DecimalField(decimal_places=13, default=0, max_digits=20, null=True),
        ),
    ]