# Generated by Django 5.0.4 on 2024-05-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0016_remove_grafic_dont_work_days_work_day_dont_work_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_li4',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='exam_li5',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='exam_li6',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='exam_li7',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='exam_li8',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='exam_li9',
        ),
        migrations.AddField(
            model_name='exam',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]