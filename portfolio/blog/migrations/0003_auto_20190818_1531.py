# Generated by Django 2.0.2 on 2019-08-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190818_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]