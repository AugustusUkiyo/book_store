# Generated by Django 3.2.4 on 2021-06-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_auto_20210616_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
