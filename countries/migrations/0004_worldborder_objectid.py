# Generated by Django 3.1.7 on 2021-04-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20210409_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldborder',
            name='objectid',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
