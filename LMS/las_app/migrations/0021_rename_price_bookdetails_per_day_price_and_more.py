# Generated by Django 5.0.1 on 2024-02-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0020_alter_daily_visitors_issue_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookdetails',
            old_name='Price',
            new_name='per_day_Price',
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='per_hour_Price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
