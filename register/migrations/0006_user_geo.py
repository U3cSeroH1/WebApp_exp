# Generated by Django 2.1.4 on 2019-01-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20190121_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='geo',
            field=models.CharField(blank=True, max_length=150, verbose_name='geo'),
        ),
    ]
