# Generated by Django 2.2.10 on 2020-06-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book language', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Enter a language for this book', to='catalog.Language'),
        ),
    ]