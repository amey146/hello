# Generated by Django 4.2.2 on 2023-08-04 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_date_flight_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='layover',
            new_name='Layover',
        ),
        migrations.AddField(
            model_name='flight',
            name='dDate',
            field=models.DateField(default=datetime.datetime(2023, 8, 4, 5, 12, 7, 777645, tzinfo=datetime.timezone.utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='dTime',
            field=models.TimeField(default=datetime.datetime(2023, 8, 4, 5, 12, 14, 713618, tzinfo=datetime.timezone.utc), max_length=30),
            preserve_default=False,
        ),
    ]
