# Generated by Django 5.0.1 on 2024-05-04 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_service_photo_service_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_text',
            name='service_text_2',
            field=models.TextField(blank=True),
        ),
    ]
