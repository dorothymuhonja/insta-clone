# Generated by Django 3.1.7 on 2021-03-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
