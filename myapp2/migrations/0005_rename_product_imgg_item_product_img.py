# Generated by Django 5.0.1 on 2024-01-25 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0004_remove_item_product_img_item_product_imgg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='product_imgg',
            new_name='product_img',
        ),
    ]
