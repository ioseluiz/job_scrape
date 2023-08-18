# Generated by Django 4.2.4 on 2023-08-18 02:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]