# Generated by Django 4.2.3 on 2023-08-22 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=255)),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('year', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('millage', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('fuel_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('transmission', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('horsepower', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('color', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('more_information', models.CharField(blank=True, default='', max_length=3000, null=True)),
                ('main_image', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='', max_length=255)),
                ('date', models.DateField(auto_now_add=True, verbose_name='')),
                ('ad', models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='Ads.ads')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=255)),
                ('ad', models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Ads.ads')),
            ],
        ),
    ]
