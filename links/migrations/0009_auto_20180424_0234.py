# Generated by Django 2.0.3 on 2018-04-24 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0008_remove_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='link',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
