# Generated by Django 4.2.1 on 2023-05-20 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_subtitledatamodel_media_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitledatamodel',
            name='SubtitleID',
            field=models.CharField(default='ec60b2c7-b4c3-4215-8bdd-ccf6ec0ab82b', max_length=36),
        ),
    ]
