# Generated by Django 2.0.2 on 2019-08-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('subtitle', models.CharField(max_length=120)),
                ('text', models.TextField()),
            ],
        ),
    ]
