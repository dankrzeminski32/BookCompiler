# Generated by Django 4.0.1 on 2022-03-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookDashboard', '0006_book_first_point_book_second_point_book_third_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='first_point_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='is_review_complete',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='second_point_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='third_point_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]