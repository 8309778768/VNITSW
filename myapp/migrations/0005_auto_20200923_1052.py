# Generated by Django 3.1.1 on 2020-09-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_book_book3'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book4',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book5',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
