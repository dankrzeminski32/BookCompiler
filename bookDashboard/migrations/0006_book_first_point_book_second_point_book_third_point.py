# Generated by Django 4.0.1 on 2022-03-01 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookDashboard', '0005_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='first_point',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='second_point',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='third_point',
            field=models.TextField(blank=True),
        ),
    ]
