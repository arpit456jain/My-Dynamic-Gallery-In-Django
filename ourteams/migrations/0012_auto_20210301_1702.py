# Generated by Django 3.1.3 on 2021-03-01 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourteams', '0011_auto_20210301_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourgallery',
            old_name='twitter_url',
            new_name='github_url',
        ),
    ]