# Generated by Django 3.2.4 on 2021-07-04 09:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_answer_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='likes',
        ),
        migrations.AddField(
            model_name='answer',
            name='userDownVotes',
            field=models.ManyToManyField(blank=True, related_name='threadDownVotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='userUpVotes',
            field=models.ManyToManyField(blank=True, related_name='threadUpVotes', to=settings.AUTH_USER_MODEL),
        ),
    ]