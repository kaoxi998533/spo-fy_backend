# Generated by Django 5.0.6 on 2024-07-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='portrait_path',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
