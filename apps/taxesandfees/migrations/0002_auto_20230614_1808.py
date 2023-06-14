# Generated by Django 3.2.6 on 2023-06-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20230614_1808'),
        ('taxesandfees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxAndFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=5, max_digits=8)),
                ('type', models.CharField(choices=[('tax', 'Tax'), ('fee', 'Fee')], max_length=50)),
                ('amount_adult', models.DecimalField(decimal_places=5, help_text='Amount charged per adult. Only applicable if amountType = fixed_per_person (Per Person Per Night)', max_digits=8, null=True)),
                ('amount_child', models.DecimalField(decimal_places=5, help_text='Amount charged per children. Only applicable if amountType = fixed_per_person (Per Person Per Night)', max_digits=8, null=True)),
                ('amount_type', models.CharField(choices=[('fixed', 'Fixed'), ('percentage', 'Percentage'), ('fixed_per_person', 'Fixed per person'), ('percentage_rate_based', 'Percentage rate based')], max_length=50)),
                ('available_for', models.JSONField()),
                ('inclusive_or_exclusive', models.CharField(choices=[('inclusive', 'Inclusive'), ('exclusive', 'Exclusive')], max_length=50)),
                ('is_deleted', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Fee',
        ),
        migrations.DeleteModel(
            name='Taxes',
        ),
    ]
