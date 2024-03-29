# Generated by Django 5.0.2 on 2024-03-17 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
