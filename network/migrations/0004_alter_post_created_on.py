# Generated by Django 4.0.4 on 2022-05-12 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
