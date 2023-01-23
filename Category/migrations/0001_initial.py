# Generated by Django 4.0.5 on 2023-01-20 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('mobile', models.IntegerField(default=1)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('price', models.IntegerField(default=1)),
                ('contact_person', models.CharField(blank=True, max_length=100)),
                ('contact_photo', models.ImageField(blank=True, upload_to='')),
                ('menu', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ListCategories',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('review', models.TextField(blank=True)),
                ('rating', models.IntegerField(choices=[(5, '*****'), (4, '****'), (3, '***'), (2, '**'), (1, '*')], default=1)),
                ('slug', models.SlugField(blank=True)),
                ('review_on', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listreview', to='Category.list')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('menutags', models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER')], default=1, max_length=100)),
                ('items', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=1)),
                ('slug', models.SlugField(blank=True, primary_key=True, serialize=False)),
                ('restaurant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantname', to='Category.list')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='catgeory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='Category.listcategories'),
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_list', models.CharField(blank=True, max_length=100)),
                ('hotelname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listname', to='Category.list')),
            ],
        ),
    ]
