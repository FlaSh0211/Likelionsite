# Generated by Django 2.1.5 on 2019-03-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='document',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
