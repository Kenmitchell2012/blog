# Generated by Django 5.0.2 on 2024-02-08 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]