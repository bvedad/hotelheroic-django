# Generated by Django 3.2.6 on 2023-06-14 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxesandfees', '0002_auto_20230614_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxandfee',
            name='available_for',
        ),
    ]