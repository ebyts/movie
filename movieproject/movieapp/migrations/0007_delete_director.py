# Generated by Django 4.2.4 on 2023-08-18 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_rename_img_director_imgd'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Director',
        ),
    ]
