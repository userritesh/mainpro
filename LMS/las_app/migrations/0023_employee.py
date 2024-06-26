# Generated by Django 5.0.1 on 2024-03-05 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las_app', '0022_rename_request_status_daily_visitors_return_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('yearly_package', models.IntegerField(blank=True, null=True)),
                ('monthly_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('Employee_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='las_app.userdetails')),
            ],
        ),
    ]
