# Generated by Django 5.0.1 on 2024-02-16 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0004_remove_issuebook_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='Charge',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='Request_genrated_by',
        ),
    ]
