# Generated by Django 4.0.2 on 2022-02-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Stock',
            field=models.IntegerField(default=10, max_length=5000),
            preserve_default=False,
        ),
    ]
