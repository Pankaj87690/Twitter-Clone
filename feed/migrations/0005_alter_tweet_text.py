# Generated by Django 4.0.3 on 2022-08-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_remove_tweet_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(default='', max_length=250),
        ),
    ]
