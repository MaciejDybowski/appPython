# Generated by Django 3.0.8 on 2020-07-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSluzby', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duty',
            old_name='typeOfDuy',
            new_name='typeOfDuty',
        ),
    ]