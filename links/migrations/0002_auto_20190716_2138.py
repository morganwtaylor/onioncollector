# Generated by Django 2.0.3 on 2019-07-17 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='link',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='links.Link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Star'), (3, '3 Star'), (4, '4 Star'), (5, '5 Star')], default=1),
        ),
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default='', max_length=250),
        ),
    ]