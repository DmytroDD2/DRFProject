# Generated by Django 4.2.5 on 2023-10-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.URLField(),
        ),
    ]
