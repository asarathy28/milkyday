# Generated by Django 3.0.8 on 2021-03-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210208_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchorder',
            name='name',
            field=models.CharField(default='hello', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchfeature',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='merchitem',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]