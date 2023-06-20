# Generated by Django 3.2.6 on 2023-06-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_auto_20230618_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Choose the language for your terms and conditions.', max_length=50)),
                ('content', models.TextField(help_text='Enter your terms and conditions. Apply format if needed.')),
            ],
            options={
                'verbose_name_plural': 'Terms and Conditions',
            },
        ),
    ]