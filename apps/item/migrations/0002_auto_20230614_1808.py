# Generated by Django 3.2.6 on 2023-06-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='item',
            name='taxes',
        ),
    ]
