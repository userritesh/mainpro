# Generated by Django 5.0.1 on 2024-02-22 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0015_remove_issuebook_request_genrated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuebook',
            name='Request_genrated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
