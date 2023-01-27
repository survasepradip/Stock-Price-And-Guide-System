# Generated by Django 3.0.7 on 2020-10-03 10:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_auto_20200923_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='full_chat',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='tweet_follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
