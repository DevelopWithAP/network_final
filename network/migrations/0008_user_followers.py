# Generated by Django 4.0.4 on 2022-05-16 07:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_rename_folowing_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
