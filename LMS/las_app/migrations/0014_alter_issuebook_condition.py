# Generated by Django 5.0.1 on 2024-02-20 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0013_rename_book_name_bookdetails_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='Condition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
