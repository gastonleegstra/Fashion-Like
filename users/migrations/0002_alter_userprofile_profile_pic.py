# Generated by Django 4.1.5 on 2023-02-07 01:29

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/default/default_avatar.jpg', upload_to=users.models.photo_up_path),
        ),
    ]
