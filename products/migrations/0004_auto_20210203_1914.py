# Generated by Django 3.1 on 2021-02-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]