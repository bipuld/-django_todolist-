# Generated by Django 4.1.6 on 2023-02-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupform',
            old_name='Time',
            new_name='date_Time',
        ),
    ]
