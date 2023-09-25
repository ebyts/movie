# Generated by Django 4.2.4 on 2023-08-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ex', upload_to='gallry'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(max_length=25),
        ),
    ]
