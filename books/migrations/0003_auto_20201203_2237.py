# Generated by Django 3.1.3 on 2020-12-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20201203_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='label',
            field=models.CharField(max_length=50),
        ),
    ]