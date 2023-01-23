# Generated by Django 4.0.5 on 2023-01-20 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
                ('posted_by', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
