# Generated by Django 4.1 on 2022-08-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_room_members_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
