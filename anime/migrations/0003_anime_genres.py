# Generated by Django 5.1.3 on 2024-12-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.JSONField(blank=True, null=True),
        ),
    ]