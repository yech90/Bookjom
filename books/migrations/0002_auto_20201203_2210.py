# Generated by Django 3.1.3 on 2020-12-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='main_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='second_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]