# Generated by Django 5.0.6 on 2024-07-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_path',
            new_name='video_file',
        ),
    ]
