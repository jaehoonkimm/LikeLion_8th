# Generated by Django 3.0.6 on 2020-06-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summer_app', '0003_auto_20200629_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(blank=True),
        ),
    ]