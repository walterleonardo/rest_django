# Generated by Django 3.1 on 2021-02-03 22:17

import apirest.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0002_auto_20210203_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='csvs', validators=[apirest.models.validate_file_extension]),
        ),
    ]
