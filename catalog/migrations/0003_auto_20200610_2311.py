# Generated by Django 2.2.10 on 2020-06-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200610_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['lastname', 'firstname']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='firstname',
        ),
    ]
