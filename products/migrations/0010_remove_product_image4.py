# Generated by Django 3.1.1 on 2020-10-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200928_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]
