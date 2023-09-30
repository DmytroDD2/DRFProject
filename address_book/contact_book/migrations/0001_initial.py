# Generated by Django 4.2.5 on 2023-09-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('url', models.URLField(unique=True)),
                ('phone', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contacts_event/')),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('dat_time', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('contacts_book', models.ManyToManyField(related_name='contact_event', to='contact_book.contactbook')),
            ],
        ),
    ]
