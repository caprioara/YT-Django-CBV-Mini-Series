# Generated by Django 3.1 on 2020-08-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
