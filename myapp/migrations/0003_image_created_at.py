# Generated by Django 4.1 on 2022-08-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
