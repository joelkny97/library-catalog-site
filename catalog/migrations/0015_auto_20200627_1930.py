# Generated by Django 2.2.10 on 2020-06-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_remove_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
