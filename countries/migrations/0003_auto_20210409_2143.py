# Generated by Django 3.1.7 on 2021-04-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20210409_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='area',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='fips',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='iso2',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='iso3',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='pop2005',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='region',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='un',
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
