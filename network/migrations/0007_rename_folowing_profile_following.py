# Generated by Django 4.0.4 on 2022-05-13 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_rename_fololwing_profile_folowing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='folowing',
            new_name='following',
        ),
    ]
