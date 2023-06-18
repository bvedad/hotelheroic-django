# Generated by Django 3.2.6 on 2023-06-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_auto_20230618_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalAndDeparture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_time', models.TimeField(help_text='Set the check-in time for your property.')),
                ('check_out_time', models.TimeField(help_text='Set the check-out time for your property.')),
                ('late_check_out_allowed', models.BooleanField(default=False, help_text='Specify whether you offer a late check-out option.')),
                ('late_check_out_time', models.TimeField(blank=True, help_text='Set the preferred late check-out time for guests.', null=True)),
                ('late_check_out_charge_type', models.CharField(blank=True, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')], help_text='Choose the type of charge for late check-out.', max_length=10)),
                ('late_check_out_charge_amount', models.DecimalField(decimal_places=2, default=0.0, help_text='Set the amount for the late check-out charge.', max_digits=8)),
            ],
        ),
    ]
