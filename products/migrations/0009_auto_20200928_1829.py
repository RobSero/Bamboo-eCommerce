# Generated by Django 3.1.1 on 2020-09-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200928_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(default='N/A', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='measurements',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]