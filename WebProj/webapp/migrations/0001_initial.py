# Generated by Django 4.1 on 2022-08-28 07:50

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('magnitude', models.FloatField()),
                ('country', models.CharField(max_length=10)),
            ],
        ),
    ]
