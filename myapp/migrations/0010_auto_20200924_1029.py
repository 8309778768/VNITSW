# Generated by Django 3.1.1 on 2020-09-24 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200923_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf1', models.FileField(upload_to='')),
                ('pdf2', models.FileField(upload_to='')),
                ('pdf3', models.FileField(upload_to='')),
                ('pdf4', models.FileField(upload_to='')),
                ('pdf5', models.FileField(upload_to='')),
                ('pdf6', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='book6',
        ),
    ]