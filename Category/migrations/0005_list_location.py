# Generated by Django 4.0.5 on 2023-01-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_bookedlist_booked_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
