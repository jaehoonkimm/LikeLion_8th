# Generated by Django 3.0.6 on 2020-07-25 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('week10_app', '0006_auto_20200725_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='writer',
        ),
    ]
