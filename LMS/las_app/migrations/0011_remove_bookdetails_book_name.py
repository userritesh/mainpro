# Generated by Django 5.0.1 on 2024-02-16 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0010_issuebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetails',
            name='Book_Name',
        ),
    ]