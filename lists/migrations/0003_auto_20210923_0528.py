# Generated by Django 2.2.5 on 2021-09-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20210923_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='room',
            field=models.ManyToManyField(blank=True, related_name='lists', to='rooms.Room'),
        ),
    ]
