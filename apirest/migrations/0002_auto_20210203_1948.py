# Generated by Django 3.1 on 2021-02-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='csvs'),
        ),
        migrations.AlterField(
            model_name='csv',
            name='uploaded',
            field=models.DateField(auto_now_add=True),
        ),
    ]
