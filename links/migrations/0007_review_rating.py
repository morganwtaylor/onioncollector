# Generated by Django 2.0.3 on 2018-04-24 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default='0'),
        ),
    ]
