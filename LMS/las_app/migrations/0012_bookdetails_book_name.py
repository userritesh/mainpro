# Generated by Django 5.0.1 on 2024-02-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0011_remove_bookdetails_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='Book_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
