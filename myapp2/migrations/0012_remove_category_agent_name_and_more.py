# Generated by Django 5.0.1 on 2024-04-05 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0011_rename_goodcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='agent_name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='block_number',
        ),
        migrations.RemoveField(
            model_name='category',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='contact_person_information',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cr_number',
        ),
        migrations.RemoveField(
            model_name='category',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='category',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='category',
            name='location',
        ),
        migrations.RemoveField(
            model_name='category',
            name='order_forms',
        ),
        migrations.RemoveField(
            model_name='category',
            name='order_forms_part_2',
        ),
        migrations.RemoveField(
            model_name='category',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='category',
            name='selection_type',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('good', 'Good'), ('normal', 'Normal')], default='normal', max_length=100),
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp2.order'),
            preserve_default=False,
        ),
    ]
