# Generated by Django 2.0.3 on 2019-07-17 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20190716_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='review',
            name='featured',
        ),
    ]
