# Generated by Django 4.0.3 on 2022-08-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_tweet_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='firstname',
        ),
    ]
