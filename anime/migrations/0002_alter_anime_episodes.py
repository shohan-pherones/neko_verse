# Generated by Django 5.1.3 on 2024-12-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='episodes',
            field=models.IntegerField(null=True),
        ),
    ]
