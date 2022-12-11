# Generated by Django 4.1.3 on 2022-11-18 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0006_remove_studio_geolocation_alter_point_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='studio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='point', to='studios.studio'),
        ),
    ]