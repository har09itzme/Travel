# Generated by Django 3.2.15 on 2022-10-11 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place1',
            old_name='description',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='place1',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='place1',
            old_name='name',
            new_name='name1',
        ),
    ]
