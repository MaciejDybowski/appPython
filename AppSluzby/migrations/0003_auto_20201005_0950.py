# Generated by Django 3.0.8 on 2020-10-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSluzby', '0002_auto_20200930_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='defaultCeremony',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='defaultDuty',
            field=models.FloatField(default=0),
        ),
    ]
