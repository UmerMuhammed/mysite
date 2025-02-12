# Generated by Django 5.0.1 on 2024-01-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_ids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ImageField(max_length=50, null=True, upload_to='')),
                ('product', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField()),
                ('product_img', models.ImageField(max_length=50, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_img', models.ImageField(upload_to='product_images/')),
            ],
        ),
    ]
