# Generated by Django 5.0.1 on 2024-02-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0006_issuebook_charge_issuebook_request_genrated_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='Charge',
        ),
    ]
