# Generated by Django 3.2.6 on 2023-06-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_taxes_and_fees'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemCategories',
            new_name='ItemCategory',
        ),
    ]
