# Generated by Django 4.1.5 on 2023-02-08 01:38

from django.db import migrations, models
import posteos.models


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posteos.models.photo_up_path),
        ),
    ]
