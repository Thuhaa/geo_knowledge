# Generated by Django 3.1.7 on 2021-04-10 13:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_worldborder_objectid'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('cntry_name', models.CharField(max_length=39)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'World Borders',
            },
        ),
        migrations.DeleteModel(
            name='WorldBorder',
        ),
    ]
