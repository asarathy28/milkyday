# Generated by Django 3.0.8 on 2021-05-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210501_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchfeature',
            name='mobile_image',
            field=models.CharField(default='temp', max_length=200),
            preserve_default=False,
        ),
    ]
