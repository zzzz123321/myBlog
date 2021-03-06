# Generated by Django 2.0.2 on 2018-03-13 08:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2018, 3, 13, 8, 35, 11, 810705, tzinfo=utc), editable=False, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2018, 3, 13, 8, 35, 33, 22649, tzinfo=utc), editable=False, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'category')},
        ),
    ]
