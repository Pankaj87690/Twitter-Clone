# Generated by Django 4.0.3 on 2022-08-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jfif', upload_to='profile_pics'),
        ),
    ]
