from django.db import migrations


def create_system_notifications(apps, schema_editor):
    SystemNotification = apps.get_model('settings', 'SystemNotification')
    choices = SystemNotification.notification_type.field.choices

    for choice in choices:
        SystemNotification.objects.create(notification_type=choice[0])


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0021_systemnotification'),
    ]

    operations = [
        migrations.RunPython(create_system_notifications),
    ]