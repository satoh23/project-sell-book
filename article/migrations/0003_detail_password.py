# Generated by Django 3.1 on 2021-08-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210808_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='password',
            field=models.CharField(default='a', max_length=100, verbose_name='パスワード'),
            preserve_default=False,
        ),
    ]
