# Generated by Django 4.1.3 on 2022-11-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0016_alter_studioclass_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioclass',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('cancelled', 'cancelled')], default='active', max_length=20),
        ),
    ]