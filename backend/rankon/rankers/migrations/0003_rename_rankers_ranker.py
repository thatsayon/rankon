# Generated by Django 5.0.3 on 2024-03-18 13:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankers', '0002_rankers_vote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rankers',
            new_name='Ranker',
        ),
    ]
